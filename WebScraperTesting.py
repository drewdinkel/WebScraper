#Library for webscraping
from bs4 import BeautifulSoup
#Library for accessing URLs
import requests
#Library to turn data into a spreadsheet for easier viewing
import csv

#Website we want to scrape
website = requests.get("https://quotes.toscrape.com")
#Converting website to text using python's standard library HTML parser
soup = BeautifulSoup(website.text, "html.parser")
#Grabs a list of quotes and their respective authors
quote = soup.findAll("span", attrs={"class":"text"})
author = soup.findAll("small", attrs={"class":"author"})

#Creating a new csv file
file = open("quotes.csv", "w")
#csv.writer is used to insert the scraped data into the newly created document
writer = csv.writer(file)

#Writes the first row which will consist of the headers
writer.writerow(["Quote", "Author"])

#Printing out the scraped data
#zip() pairs together values that are at the same index
for q, a in zip(quote, author):
    #Prints quote and author
    print(q.text + " - " + a.text)
    #Adding the quote and author to the spreadsheet
    writer.writerow([q.text, a.text])

#Close the file
file.close()