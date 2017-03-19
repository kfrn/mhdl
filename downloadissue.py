#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup

def download_mag_issue(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    download_options = soup.find_all(class_='download-pill')
    proc_jp2 = download_options[7]

    download_link = "https://archive.org" + proc_jp2.get('href')

    print(download_link)
    return download_link

download_mag_issue("https://archive.org/details/pictureplayweekl01unse")
