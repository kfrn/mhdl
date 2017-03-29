#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import csv
import os
import shutil
import pandas as pd

def get_issue_list():
    issues = []
    data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
    for row in data:
        issues.append(row[6])
    return list(set(issues))

def get_download_page(input):
    # Ignore blanks, header row, and any random values passed as inputs
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
            zfile.extractall('./images/%s_jp2' % input)
    print("Download and extraction complete. Check the images/%s_jp2 subfolder." % input)

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
    # unzip_folder(full_dl_path, input)


def does_imgfolder_exist(img_path):
    return os.path.isdir(img_path)

def get_path_to_imgs(outer_folder):
    return outer_folder + os.listdir(outer_folder)[0]

def copyRelImageFiles(input):
    outer_img_folder = './images/%s_jp2/' % issue

    if not does_imgfolder_exist(outer_img_folder):
        print("There's no image folder related to that issue. Exiting")
        return

    path_to_imgs = get_path_to_imgs(outer_img_folder)

    csv_data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
    for row in csv_data:
        vol = row[0]
        no = row[1]
        if row[2] != "":
            day = row[2]
        else:
            day = "noday"
        month = row[3]
        year = row[4]
        book_id = row[6]
        jp2_img = row[7]
        output_filename = "Picture-Play_vol" + vol + "_no" + no + "_" + day + "-" + month + "-" + year + ".jp2"
        if book_id == issue:
            shutil.copy2("%s/%s" % (path_to_imgs, jp2_img), "./jp2_images/%s" % output_filename)
            print("Output file created in the jp2_images directory:", output_filename)
            # Now ... write the filename to column in the CSV?


# TESTING ..... #
# issue = "Picture-playMagazineJan.1922"
# issue = "obviously-fake"
issue = "pictureplayweekl01unse"
download_mag_issue(issue)
copyRelImageFiles(issue)

mag_issues = get_issue_list()

# # Actual call
# for issue in mag_issues:
#     download_mag_issue(issue)
#     copyRelImageFiles(issue)
