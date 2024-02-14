#Library for webscraping
from bs4 import BeautifulSoup
#Library for accessing URLs
import requests
#Library to turn data into a spreadsheet for easier viewing
import csv
#Library for command line arguments
import argparse

#Setting userAgent to avoid 403 Forbidden error
userAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

#Sets base url to no genre
base_url = "https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries"

#Creates argparse object
parser = argparse.ArgumentParser()
#Adding argument
parser.add_argument('--genre', type=str)
args = parser.parse_args()

#If the user didn't input a genre none is set
if (args == None):
    url = base_url
#If the user inputted a genre the genre(s) are set
else:
    url = base_url + "&genres=" + args

#Website we want to scrape
site = requests.get(url, headers=userAgent)

#Converting website to text using python's standard library HTML parser
soup = BeautifulSoup(site.text, "html.parser")
#Important information getting scraped
title = soup.findAll("h3", attrs={"class":"ipc-title__text"})
rating = soup.findAll("span", attrs={"class":"ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating"})
description = soup.findAll("div", attrs={"class":"ipc-html-content-inner-div"})

#Creating a new csv file
file = open("IMDb_Shows.csv", "w")
#csv.writer is used to insert the scraped data into the newly created document
writer = csv.writer(file)
#Writes the headers for the csv file (First row of the csv file)
writer.writerow(["Title", "Rating (w/ Vote Count)", "Description"])

#Inputting data to csv file
#zip() pairs together values that are at the same index
for t, r, d in zip(title, rating, description):
    #Adds the scraped information to the csv file in order
    writer.writerow([t.text, r.text, d.text])

#Closing the file
file.close()