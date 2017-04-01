#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import csv

from get_issue_list import get_issue_list

def get_download_page(input):
    if "picture" in input or "Picture" in input:
        return "https://archive.org/details/" + input
    else:
        print("Input doesn't contain the relevant string. Exiting")

def get_download_path(links):
    if len(links) == 0:
        print("No relevant download links found. Exiting")
        return
    elif len(links) == 1:
        return "https://archive.org" + links[0]
    elif len(links) == 2:
        return "https://archive.org" + links[1]
    else:
        print("More than two jp2-related downloads? That's odd. You should check that out.")
        return

def unzip_folder(path_to_folder, input):
    with urlopen(path_to_folder) as zip_response:
        with ZipFile(BytesIO(zip_response.read())) as zfile:
            zfile.extractall('./issue_downloads/%s_jp2' % input)
    print("Download and extraction complete. Check the issue_downloads/%s_jp2 subfolder." % input)

def download_mag_issue(input):
    url = get_download_page(input)
    if not url:
        return

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')

    downloads = soup.find_all(class_='download-pill')
    download_links = []
    for dlink in downloads:
        download_links.append(dlink.get('href'))
    download_links = [x for x in download_links if 'jp2' in x]

    full_dl_path = get_download_path(download_links)
    if not full_dl_path:
        return

    print("Downloading and unzipping %s. This will take a while. Stand by ..." % full_dl_path)
    unzip_folder(full_dl_path, input)


mag_issues = get_issue_list()

for issue in mag_issues:
    download_mag_issue(issue)
