print("Checkpoint 1.")

#Library for webscraping
from bs4 import BeautifulSoup
#Library for accessing URLs
import requests
#Library to turn data into a spreadsheet for easier viewing
import csv

print("Checkpoint 2.")

#Target website being scraped
site = requests.get("https://www.imdb.com/list/ls023983860/")
#Converting website to text using python's standard library HTML parser
soup = BeautifulSoup(site.text, "html.parser")

print("Checkpoint 3.")

#Scraping all important information (Show Name, Genre(s), Rating, Show Description)
name = soup.findAll("a", attrs={"href"})
genre = soup.findAll("span", attrs={"class":"genre"})
rating = soup.findAll("span", attrs={"class":"ipl-rating-star__rating"})
description = soup.findAll("p", attrs={"class"})

print("Checkpoint 4.")

#Loop to print all scraped information
for n, g, r, d in zip(name, genre, rating, description):
    print("Checkpoint 5.")
    print(n.text + "\n" + g.text + "\n" + r.text + "\n" + d.text)
    print("Checkpoint 6.")

#Name does not work at all (Printing file location???)
#Genre works
#Rating kind of works (Prints rating but also "Rate" which we dont want)
    #Potentially add counter variable because it seems to only print "Rate" after the actual rating
#Description does not work at all (Printing file location???)