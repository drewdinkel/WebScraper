from bs4 import BeautifulSoup
import requests
#Importing argparse library
import argparse

userAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

#Creates argparse object
parser = argparse.ArgumentParser(description="Find quotes on specific page")
#Adding arguments (-page means this is an optional argument)
#metavar is the name that shows up when -h command is used
parser.add_argument("-page", metavar="--page", type=str, help="Enter your page number")
args = parser.parse_args()
#Variable being changed to alter website getting accessed
page = args.page

#Valid argument would be:
#python3 argparseTesting.py --page /page/2/

#if condition that checks if page is empty (equal to None)
if (page == None):
    page = "/page/1/"

url = "https://quotes.toscrape.com" + page

website = requests.get(url, headers=userAgent)

soup = BeautifulSoup(website.text, "html.parser")
quote = soup.findAll("span", attrs={"class":"text"})
author = soup.findAll("small", attrs={"class":"author"})

for q, a in zip(quote, author):
    print(q.text + " - " + a.text)