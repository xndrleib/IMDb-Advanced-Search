# IMDb Advanced Search

A Python package for building and filtering IMDb search URLs based on various criteria.

## Description

**IMDb Advanced Search** is a Python package designed to help users create customized IMDb search URLs with a variety of filters. Whether you're looking to find movies by specific genres, countries, ratings, or other criteria, this tool streamlines the process, allowing for precise and efficient searches on IMDb.

## Features

- **Genre Filtering:** Include or exclude specific genres in your search.
- **Vote Count:** Set minimum and maximum number of votes.
- **User Rating:** Define rating ranges between 1.0 to 10.0.
- **Release Date:** Specify start and end release dates in `YYYY-MM-DD` format.
- **Country Filtering:** Include or exclude countries using IMDb country codes.
- **Runtime Constraints:** Set minimum and maximum runtime in minutes.
- **Sorting Options:** Sort results by popularity, user rating, or number of votes in ascending or descending order.
- **Title Types:** Filter by title types such as feature films, TV series, shorts, etc.
- **Keyword Exclusion:** Exclude specific keywords from your search.
- **Awards Filter:** Option to include only titles with awards.

## Installation

### Steps

1. **Clone the Repository:**

    ```bash
    git clone https://github.com/xndrleib/IMDb-Advanced-Search.git
    cd IMDb-Advanced-Search
    ```

2. **Set Up a Conda Environment:**

    ```bash
    conda env create --file=environment.yml -y
    ```
3. **Activate the Environment:**
    ```
    conda activate imdb_env
    ```

## Configuration

Customize your search parameters by editing the `config/search_query.yml` file. Below is an example configuration:

```yaml
include_genres:
  - action
  - comedy
exclude_genres:
  - horror
min_votes: 1000
max_votes: 50000
min_rating: 7.0
max_rating: 9.5
start_date: 2020-01-01
end_date: 2024-12-31
include_countries:
  - United States
  - United Kingdom
exclude_countries:
  - Canada
min_runtime: 90
max_runtime: 180
sort_type: moviemeter
sort_option: asc
title_type:
  - feature
  - tv_series
exclude_keywords:
  - remake
  - sequel
```

### Parameters

- **include_genres:** List of genres to include.
- **exclude_genres:** List of genres to exclude.
- **min_votes & max_votes:** Vote count range.
- **min_rating & max_rating:** User rating range.
- **start_date & end_date:** Release date range in `YYYY-MM-DD`.
- **include_countries & exclude_countries:** Countries to include or exclude.
- **min_runtime & max_runtime:** Runtime range in minutes.
- **sort_type & sort_option:** Sorting criteria and order.
- **title_type:** Types of titles to include (e.g., feature, tv_series).
- **exclude_keywords:** Keywords to exclude from the search.

## Usage

Run the `search.py` script to generate the IMDb search URL based on your configuration:

```bash
python search.py
```

The script will read the parameters from `config/search_query.yml`, construct the search URL, and print it to the console. You can then use this URL to perform an advanced search on IMDb.

### Example Output

```
https://www.imdb.com/search/title/?genres=action,comedy,!horror&num_votes=1000,50000&user_rating=7.0,9.5&release_date=2020-01-01,2024-12-31&countries=us,!ca&runtime=90,180&sort=moviemeter,asc&title_type=feature,tv_series&keywords=!remake,!sequel&has=awards
```

## Directory Structure

```
IMDb-Advanced-Search/
├── .gitignore
├── config/
│   └── search_query.yml
├── environment.yml
├── search.py
├── setup.py
├── valid_parameters.py
└── README.md
```

- **.gitignore:** Specifies files and directories to ignore in the repository.
- **config/search_query.yml:** YAML configuration file containing search parameters.
- **environment.yml:** Conda environment configuration file.
- **search.py:** Main script to generate the IMDb search URL.
- **valid_parameters.py:** Contains valid genres and country codes for validation.
- **README.md:** Documentation file.
