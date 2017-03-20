#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile

def download_mag_issue(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    download_options = soup.find_all(class_='download-pill')
    proc_jp2_link = download_options[7].get('href')
    zip_filename = proc_jp2_link.split('/')[-1]
    filename = zip_filename.split('.')[0]

    download_url = "https://archive.org" + proc_jp2_link

    print("Downloading and unzipping %s. Stand by ..." % zip_filename)

    with urlopen(download_url) as zip_response:
        with ZipFile(BytesIO(zip_response.read())) as zfile:
            zfile.extractall(filename)

    print("Download and extraction of %s complete. Check the %s subfolder." % (zip_filename, filename))

download_mag_issue("https://archive.org/details/pictureplayweekl01unse")
