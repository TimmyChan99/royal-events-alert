import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, source_name, config):
        self.source_name = source_name
        self.base_url = config['base_url']
        self.list_urls = config['urls']
        self.selectors = config['section_selectors']

    def fetch_page(self, url):
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    