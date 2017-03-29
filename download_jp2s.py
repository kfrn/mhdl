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

def get_download_url(input):
    # Ignore blanks, header row, and any random values passed as inputs
    if "picture" in input or "Picture" in input:
        return "https://archive.org/details/" + input
    else:
        print("Input doesn't contain the relevant string. Exiting")

def download_mag_issue(input):
    url = get_download_url(input)
    if not url:
        return

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

def does_imgfolder_exist(img_path):
    return os.path.isdir(img_path)

def copyRelImageFiles(input):
    outer_img_folder = './images/%s_jp2/' % issue

    # does the image folder exist?
    if not does_imgfolder_exist(outer_img_folder):
        print("There's no image folder related to that issue. Exiting")
        return

    # get the inner image folder, i.e. actual image location.
    inner_img_folder = os.listdir(outer_img_folder)[0]
    path_to_imgs = "%s%s" % (outer_img_folder, inner_img_folder)

    print("Path to images is %s" % path_to_imgs)

    # Then parse csv.
    # Where the issue name ('issue') matches the entry in the BookID column ...
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


# TESTING ..... #
issue = "Picture-playMagazineJan.1922"
# issue = "obviously-fake"
# issue = "pictureplayweekl01unse"
download_mag_issue(issue)
copyRelImageFiles(issue)

# # Actual call
# for issue in mag_issues:
#     download_mag_issue(issue)
#     copyRelImageFiles(issue)
