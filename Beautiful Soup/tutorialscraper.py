import requests
import time
from bs4 import BeautifulSoup

# Define the homepage url
homepage_url = "https://www.scrapethissite.com/pages/"
# Download the homepage
homepage = requests.get(homepage_url)
# Create a Beautiful Soup object
homepage_soup = BeautifulSoup(homepage.content, features="lxml")

# Listing Links:

# Create a list of urls linked to from the homepage
links = homepage_soup.find_all('a')

print("-----Building full urls:-----")


for  link in links:
     # print each path retrieved as a full url
     print("https://www.scrapethissite.com" + link.get('href'))

# Filtering Links:

print("-----Filtering:-----")

# we'll store the desired pages in here as we find them
pages_links = []

for  link in links:
    # get the text of the url from the link item
    url = link.get('href')
    # if the url path starts with /pages/, we'll add it to the new list
    if (url.startswith("/pages/") and len(url) > 7):
        pages_links.append(link)
        print(link.get('href'))

# Scraping Text:

print("-----Text Scraping-----")

# print entire webpage's readable text (comment in if you'd like to see it)
# print(homepage_soup.get_text("|", strip=True))

texts = homepage_soup.find_all('p')

for text in texts:
    # print each paragraphs corresponding text
    print(text.string)

# Combining Techniques: Scraping sites at links

print("-----Combining Techniques-----")

# collect the links from the present site and generate full urls
c_links = homepage_soup.find_all('a')
c_urls = []

# separate the links we want from those we dont and generate urls to visit
for  link in c_links:
     # get the text of the url from the link item
     url = link.get('href')
     # if the url path starts with /pages/, we'll add it to the new list
     if (url.startswith("/pages/") and len(url) > 7):
         c_urls.append("https://www.scrapethissite.com" + url)

# visit those urls and write to a file
with open('pagecontents.txt', 'w') as file:
    for url in c_urls:
        # set up an object to visit the page
        page = requests.get(url)
        page_soup = BeautifulSoup(page.content, features="lxml")

        # print the pages
        file.write(page_soup.get_text(" ", strip=True))

        # a delay to make sure our script doesn't overload the site's servers
        time.sleep(5)
