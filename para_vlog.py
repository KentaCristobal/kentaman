# import requests
# result=requests.get('https://kentacristobal.com/')
# print(result)
import urllib.request
from bs4 import BeautifulSoup

class Scraper():
    def __init__(self,site):
        self.site=site

    def scrape(self):
        r=urllib.request.urlopen(self.site)
        html= r.read()
        parser = 'html . parser'
        sp = BeautifulSoup(html , parser)
        for tag in sp.find_all('a') :
            url=tag.get('href')
            if url is none:
                continue
            if 'html'in url:
                print('\n' + url)
news='https://kentacristobal.com'
Scraper (news).scrape()
