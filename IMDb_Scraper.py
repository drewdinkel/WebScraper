#Library for webscraping
from bs4 import BeautifulSoup
#Library for accessing URLs
import requests

#Setting userAgent to avoid 403 Forbidden error
userAgent = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 OPR/106.0.0.0"}

#Website we want to scrape
website = requests.get("https://www.imdb.com/search/title/?title_type=tv_series,tv_miniseries", headers=userAgent)
print(website.status_code)
print(website.request.headers)

#Converting website to text using python's standard library HTML parser
soup = BeautifulSoup(website.text, "html.parser")
print(soup.prettify())