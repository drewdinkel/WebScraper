# 2024 CSHS Cybersecurity Web Scraping Project

A python program that scrapes IMDb's top TV Series by genre page using the genre(s) inputted by the user. The scraped results are compiled into a .csv file for easy viewing.

There are no additional files/dependencies needed to run this program.

## Command Line Arguments
There is only one optional argument for this program. It can be called using either "-g" or "--genre".

- -g = Adds a genre/genres the user wants to specifically search for
- --genre = Adds a genre/genres the user wants to specifically search for

If multiple genres are inputed they must be seperated by a single comma with no space inbetween.

Examples:
- python3 IMDb_Scraper
- python3 IMDb_Scraper -g action
- python3 IMDb_Scraper --genre comedy,sci-fi

## Limitations
- Currently only works with TV Series, not movies. (Could later be implemented by adding an additional command line argument)
- If too many genres are inputted there will be no results returned as shows will not match every inputted genre.
