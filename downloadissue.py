#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import csv
import os
import shutil

# Get the list of issues to download
mag_issues = []
data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
for row in data:
    mag_issues.append(row[6])
mag_issues = list(set(mag_issues))
# print(mag_issues)

def getDownloadURL(input):
    # Ignore blanks, header row, and any random values passed as inputs
    if "picture" in input or "Picture" in input:
        return "https://archive.org/details/" + input
    else:
        print("Input doesn't contain the relevant string. Exiting")

def download_mag_issue(input):
    url = getDownloadURL(input)
    if not url:
        return
    else:
        print(url)

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    downloads = soup.find_all(class_='download-pill')
    download_links = []
    for dlink in downloads:
        download_links.append(dlink.get('href'))
    download_links = [x for x in download_links if 'jp2' in x]

    if len(download_links) == 0:
        print("No relevant download links found. Exiting")
        return
    elif len(download_links) == 1:
        download_path = download_links[0]
    elif len(download_links) == 2:
        download_path = download_links[1]
    else:
        print("More than two jp2-related downloads? That's odd. You should check that out.")
        return

    full_dl_link = "https://archive.org" + download_path

    print("Downloading and unzipping %s. This will take a while. Stand by ..." % full_dl_link)

    # with urlopen(full_dl_link) as zip_response:
    #     with ZipFile(BytesIO(zip_response.read())) as zfile:
    #         zfile.extractall('./images/%s_jp2' % input)
    #
    # print("Download and extraction complete. Check the images/%s_jp2 subfolder." % input)


# TESTING ..... #
issue = "Picture-playMagazineJan.1922"
# issue = "obviously-fake"
# issue = "pictureplayweekl01unse"
download_mag_issue(issue)

# # Actual call
# for issue in mag_issues:
#     download_mag_issue(issue)

# outer_img_path = './images/%s_jp2/' % issue
