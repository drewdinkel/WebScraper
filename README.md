# 2024 CSHS Cybersecurity Web Scraping Project

A python program that scrapes IMDb's top TV Series/Movies by genre page using the genre(s) inputted by the user. The scraped results are compiled into a .csv file for easy viewing.

There are no additional files/dependencies needed to run this program.

## Command Line Arguments
There are two optional arguments for this program. One that specificies TV Shows/Movies and another that adds genres.

- -t OR --type = Specifices the type of media the user is looking for. "tv" and "movie" are valid arguments, with anything else defaulting to both types.
- -g OR --genre = Specifies the genres the user is looking for. If multiple genres are implemented they must be seperated by a comma **without space** inbetween.

Examples:
- python3 IMDb_Scraper.py
- python3 IMDb_Scraper.py -g action --type movie
- python3 IMDb_Scraper.py -t tv --genre comedy
- python3 IMDb_Scraper.py -g comedy,sci-fi

## Limitations
- If too many genres are inputted there will be no results returned as shows will not match every inputted genre.
- Ratings will be wrong in the case that one of the TV Shows/Movies have yet to be released. The TV Show/Movie has yet to recieve a rating and therefor will take the rating of the next show and cause the ratings to be offset going forward.
