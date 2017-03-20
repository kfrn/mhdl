#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import urllib.request
import shutil

def download_mag_issue(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    download_options = soup.find_all(class_='download-pill')
    proc_jp2_link = download_options[7].get('href')
    filename = proc_jp2_link.split('/')[-1]

    download_url = "https://archive.org" + proc_jp2_link

    print("Downloading %s. Stand by ..." % filename)
    # urllib.request.urlretrieve(download_url, filename) # Also works
    with urllib.request.urlopen(download_url) as response, open(filename, 'wb') as out_file:
        shutil.copyfileobj(response, out_file)
    print("Download of %s complete." % filename)

download_mag_issue("https://archive.org/details/pictureplayweekl01unse")
