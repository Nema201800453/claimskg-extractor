import pandas as pd
from bs4 import BeautifulSoup
import urllib2


def get_all_claims(criteria):
    claims = []

    url = 'https://apublica.org/checagem/'
    user_agent = 'Mozilla/5.0'
    request = urllib2.urlopen(urllib2.Request(url, data=None, headers={'User-Agent': user_agent}))
    page = request.read()
    soup = BeautifulSoup(page, 'lxml')

    pages_links = soup.findAll('a', {"class": "page-link"})
    number_of_pages = int(pages_links[::-1][1].text)
    print('Number of pages: ' + str(number_of_pages))

    pdf = pd.DataFrame(claims)
    return pdf
