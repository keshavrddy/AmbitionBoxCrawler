import requests
from bs4 import BeautifulSoup
from configuration import ambitionboxconfig as cfg
import json

class Companyreviews:

    def __init__(self, url):
        self.url = url
        self.html = requests.get(self.url, proxies=cfg.proxies, headers=cfg.headers)
        self.soup = BeautifulSoup(self.html.content, 'lxml')
        self.reviews = self.get_totalReview(self.soup)
        self.reviews.update(self.get_overallRatings(self.soup))
        self.reviews.update(self.get_otherReviews(self.soup))

    def __repr__(self):
        return repr(json.dumps(self.reviews, ensure_ascii=False))


    def get_totalReview(self, soup):
        try:
            review = {"CompanyName":soup.find('p',
                       {'class': 'card-title'}).text.strip(),
                        "TotalReview": soup.find('p',
                              {'class': 'card-title'}).span.text.strip()
            }
        except:
            review = ''
        return  review

    def get_overallRatings(self, soup):
        try:
            overall_ratings = {
                "overall rating":
                soup.find('div', {'class','rating__display__text'}).text
            }
        except:
            overall_ratings = ''
        return overall_ratings

    def get_otherReviews(self, soup):
        try:
            tag = soup.find('div', {'class','ratings_display_wrap'}).find_all('div', {'class':'rating_display'})
            ratings = { x.find('p').text : x.find('div', {'class':'span_text_wrap'}).text for x in tag}
        except:
            ratings = ''

        return ratings



