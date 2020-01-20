# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup

class WorldexampleSpider(scrapy.Spider):
    name = 'worldexample'
    allowed_domains = ['https://scrapethissite.com/pages/simple/']
    start_urls = ['https://scrapethissite.com/pages/simple/']

    def parse(self, response):
        print("\n"*2)

        soup = BeautifulSoup(response.text, 'html.parser')
        countryList = soup.find_all("div", {"class":"col-md-4 country"})

        for country in countryList:
            print(country.text.strip())
            print("\n")

        print("Total Countries Scraped: " + str(len(countryList)))
        print("\n"*2)
