# IMDb Advanced Search

IMDb Advanced Search is a Python package for building customized IMDb search URLs based on various criteria. Use it to create advanced IMDb search links with filters for genres, ratings, release dates, runtime, countries, and more!

## Description

IMDb Advanced Search streamlines the process of constructing IMDb search URLs with numerous filters. Whether you want to search for movies with specific genres, ratings, runtime, or any other criteria, this tool offers a simple yet powerful solution to build your custom queries.

## Features

- **Genre Filtering:** Include or exclude specific genres.
- **Vote Count:** Set minimum and maximum number of votes.
- **User Rating:** Define a rating range (1.0 to 10.0).
- **Release Date:** Specify start and end release dates (`YYYY-MM-DD`).
- **Country Filtering:** Filter by including or excluding specific countries (using IMDb country codes).
- **Runtime Constraints:** Set minimum and maximum runtime in minutes.
- **Sorting Options:** Sort results by popularity, user rating, or vote count in ascending or descending order.
- **Title Types:** Filter by title types such as feature films, TV series, shorts, etc.
- **Keyword Exclusion:** Exclude specific keywords from your search.
- **Awards Filter:** Optionally limit results to titles with awards.
- **CLI Configuration:** Specify a custom YAML configuration file via a command-line argument.

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

    ```bash
    conda activate imdb_env
    ```

## Configuration

Customize your search parameters by editing the YAML configuration file. By default, the script uses `config/default_query.yml`. You can also specify a different configuration file using the `--config` command-line argument.

### Example Configuration (`config/default_query.yml`)

```yaml
title_type:
  - feature
exclude_genres:
  - documentary
  - reality-tv
  - short
  - talk-show
  - music
  - musical
  - romance
  - animation
  - game-show
  - western
min_votes: 10000
min_rating: 7.0
max_rating: 10.0
start_date: 1995-01-01
end_date: 2025-12-31
exclude_countries:
  - India
  - Turkey
  - Mexico
min_runtime: 60
max_runtime: 120
sort_type: user_rating
sort_option: desc
exclude_keywords:
  - sitcom
  - sitcom-comedy
  - teenager
  - teen-drama
```

#### Parameters

- **title_type:** List of IMDb title types (e.g., `feature`, `tv_series`).
- **include_genres / exclude_genres:** Genres to include or exclude.
- **min_votes / max_votes:** Minimum and maximum vote counts.
- **min_rating / max_rating:** User rating range.
- **start_date / end_date:** Release date range in `YYYY-MM-DD`.
- **include_countries / exclude_countries:** List of countries to include or exclude.
- **min_runtime / max_runtime:** Runtime range in minutes.
- **sort_type / sort_option:** Sorting criteria and order.
- **exclude_keywords:** Keywords to exclude from the search.

## Usage

Run the `search.py` script to generate an IMDb search URL based on your configuration. You can specify a custom YAML configuration file using the `--config` argument.

### Default Usage

```bash
python search.py
```

This uses the default configuration file at `config/default_query.yml`.

### Specifying a Custom Configuration

```bash
python search.py --config path/to/your_config.yml
```

### Example Output

```
https://www.imdb.com/search/title/?genres=!documentary,!reality-tv,!short,!talk-show,!music,!musical,!romance,!animation,!game-show,!western&num_votes=10000,&user_rating=7.0,10.0&release_date=1995-01-01,2025-12-31&countries=!in,!tr,!mx&runtime=60,120&sort=user_rating,desc&title_type=feature&keywords=!sitcom,!sitcom-comedy,!teenager,!teen-drama&has=awards
```

## Directory Structure

```
IMDb-Advanced-Search/
├── .gitignore
├── config/
│   └── default_query.yml
├── environment.yml
├── search.py
├── valid_parameters.py
└── README.md
```

- **.gitignore:** Specifies files and directories to ignore.
- **config/default_query.yml:** YAML configuration file for search parameters.
- **environment.yml:** Conda environment configuration file.
- **search.py:** Main script that generates the IMDb search URL.
- **valid_parameters.py:** Contains valid genres and country codes.
- **README.md:** This documentation file.

## Contributing

Contributions are welcome! Please open issues or submit pull requests for improvements and bug fixes.