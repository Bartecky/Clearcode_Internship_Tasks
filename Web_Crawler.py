import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pprint


def site_url(web_url):
    links = [web_url]
    result = {}
    for web in links:
        sub_links = set()
        scrap_web = requests.get(web).content
        soup = BeautifulSoup(scrap_web, 'html.parser')
        for url in soup.find_all('a', href=True):
            link = urljoin(web, url.get('href'))
            if link in links:
                sub_links.add(link)
            if link not in links and web_url in link:
                links.append(link)
                sub_links.add(link)
        result[web] = {
            'title': soup.title.text,
            'links': sub_links
        }
    return result


result = site_url("http://0.0.0.0:8000")
pprint.pprint(result)
