from urllib.parse import urlencode
import yaml

import re
from valid_parameters import COUNTRY_NAME_TO_CODE, VALID_GENRES

def convert_country_names_to_codes(country_names):
    """
    Converts a list of country names to their IMDb country codes.

    Parameters:
        country_names (list of str): List of country names.

    Returns:
        list of str: IMDb country codes.

    Raises:
        ValueError: If any country name is invalid.
    """
    codes = []
    for name in country_names:
        code = COUNTRY_NAME_TO_CODE.get(name)
        if code:
            codes.append(code)
        else:
            raise ValueError(f"Invalid country name: {name}")
    return codes

def create_imdb_search_url(include_genres=None, exclude_genres=None, min_votes=None, max_votes=None, 
                           min_rating=None, max_rating=None, start_date=None, end_date=None, 
                           include_countries=None, exclude_countries=None, min_runtime=None, max_runtime=None,
                           sort_type=None, sort_option=None, title_type=None):
    """
    Creates an IMDb search URL with the specified filters.

    Parameters:
        include_genres (list of str): Genres to include in the search.
        exclude_genres (list of str): Genres to exclude from the search.
        min_votes (int): Minimum number of votes.
        max_votes (int): Maximum number of votes.
        min_rating (float): Minimum rating (1.0 to 10.0).
        max_rating (float): Maximum rating (1.0 to 10.0).
        start_date (str): Start release date in YYYY-MM-DD format.
        end_date (str): End release date in YYYY-MM-DD format.
        include_countries (list of str): Countries to include.
        exclude_countries (list of str): Countries to exclude.
        min_runtime (int): Minimum runtime in minutes.
        max_runtime (int): Maximum runtime in minutes.
        sort_type (str): Sorting type (popularity, user_rating, num_votes).
        sort_option (str): Sorting option (asc or desc).
        title_type (list of str): List of title types (e.g., feature, tv_series, etc.).

    Returns:
        str: The IMDb search URL.
    """
    query_params = {}
    
    # Genres
    include_genres = include_genres or []
    exclude_genres = exclude_genres or []
    invalid_genres = [genre for genre in include_genres + exclude_genres if genre not in VALID_GENRES]
    if invalid_genres:
        raise ValueError(f"Invalid genres specified: {', '.join(invalid_genres)}")
    formatted_genres = [genre for genre in include_genres] + [f"!{genre}" for genre in exclude_genres]
    if formatted_genres:
        query_params["genres"] = ",".join(formatted_genres)
    
    # Vote count
    if min_votes is not None or max_votes is not None:
        query_params["num_votes"] = f"{min_votes or ''},{max_votes or ''}"
    
    # User rating
    if min_rating is not None or max_rating is not None:
        if (min_rating and not 1.0 <= min_rating <= 10.0) or (max_rating and not 1.0 <= max_rating <= 10.0):
            raise ValueError("Rating must be between 1.0 and 10.0")
        query_params["user_rating"] = f"{min_rating or ''},{max_rating or ''}"
    
    # Release date
    date_pattern = r"\d{4}-\d{2}-\d{2}"
    if start_date and not re.match(date_pattern, start_date):
        raise ValueError("Start date must be in YYYY-MM-DD format")
    if end_date and not re.match(date_pattern, end_date):
        raise ValueError("End date must be in YYYY-MM-DD format")
    if start_date or end_date:
        query_params["release_date"] = f"{start_date or ''},{end_date or ''}"
    
    # Countries
    include_countries = convert_country_names_to_codes(include_countries or [])
    exclude_countries = convert_country_names_to_codes(exclude_countries or [])
    formatted_countries = [country for country in include_countries] + [f"!{country}" for country in exclude_countries]
    if formatted_countries:
        query_params["countries"] = ",".join(formatted_countries)

    # Runtime
    if min_runtime is not None or max_runtime is not None:
        query_params["runtime"] = f"{min_runtime or ''},{max_runtime or ''}"
    
    # Sorting
    if sort_type and sort_option:
        valid_sort_types = {"moviemeter", "user_rating", "num_votes"}
        valid_sort_options = {"asc", "desc"}
        if sort_type not in valid_sort_types:
            raise ValueError(f"Invalid sort type. Valid types are: {', '.join(valid_sort_types)}")
        if sort_option not in valid_sort_options:
            raise ValueError(f"Invalid sort option. Valid options are: {', '.join(valid_sort_options)}")
        query_params["sort"] = f"{sort_type},{sort_option}"

    # Title type
    if title_type:
        valid_title_types = [
            "feature", "tv_series", "short", "tv_episode", "tv_miniseries", "tv_movie", 
            "tv_special", "video_game", "video", "music_video", "podcast_series", 
            "podcast_episode", "tv_short"
        ]
        invalid_title_types = [tt for tt in title_type if tt not in valid_title_types]
        if invalid_title_types:
            raise ValueError(f"Invalid title types specified: {', '.join(invalid_title_types)}")
        query_params["title_type"] = ",".join(title_type)

    # Construct the URL
    base_url = "https://www.imdb.com/search/title/"
    full_url = f"{base_url}?{urlencode(query_params)}"
    
    return full_url

def main():
    with open("config/search_query.yml") as stream:
        try:
            query_parameters = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)


    url = create_imdb_search_url(
        include_genres=query_parameters['include_genres'],
        exclude_genres=query_parameters['exclude_genres'],
        min_votes=query_parameters['min_votes'],
        max_votes=query_parameters['max_votes'],
        min_rating=query_parameters['min_rating'],
        max_rating=query_parameters['max_rating'],
        start_date=query_parameters['start_date'].strftime('%Y-%m-%d'),
        end_date=query_parameters['end_date'].strftime('%Y-%m-%d'),
        include_countries=query_parameters['include_countries'],
        exclude_countries=query_parameters['exclude_countries'],
        min_runtime=query_parameters['min_runtime'],
        max_runtime=query_parameters['max_runtime'],
        sort_type=query_parameters['sort_type'],
        sort_option=query_parameters['sort_option'],
        title_type=query_parameters['title_type']
    )
    exclude_keywords = query_parameters['exclude_keywords']
    exclude_keywords_str = '&keywords='
    first = True
    for exclude_keyword in exclude_keywords:
        if first:
            exclude_keywords_str += f'!{exclude_keyword}'
            first = False
        else:
            exclude_keywords_str += f',!{exclude_keyword}'

    url += exclude_keywords_str
    url += '&has=awards'
    print(url)

if __name__ == '__main__':
    main()