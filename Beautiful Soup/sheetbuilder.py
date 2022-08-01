import requests
import csv
from bs4 import BeautifulSoup

# Define the homepage url
homepage_url = "https://www.scrapethissite.com/pages/simple/"
# Download the homepage
homepage = requests.get(homepage_url)
# Create a Beautiful Soup object
homepage_soup = BeautifulSoup(homepage.content, features="lxml")

countries = homepage_soup.find_all(class_ = "col-md-4 country")


with open('sheetcontents.csv', 'w') as file:
    # Create a writer
    writer = csv.writer(file)
    # Create a header row
    writer.writerow(['Country', 'Capital', 'Population', 'Area'])

    for country in countries:
        # Find and store the relevant data in variables
        c_name = country.h3.contents[2].get_text(strip=True)
        c_capital = country.div.find(class_ = "country-capital").contents[0]
        c_population = country.div.find(class_ = "country-population").contents[0]
        c_area = country.div.find(class_ = "country-area").contents[0]

        # Add a new row to the spreadsheet with this data
        writer.writerow([c_name, c_capital, c_population, c_area])
