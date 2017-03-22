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

def download_mag_issue(input):

    # Ignore blanks, header row, and any random values passed as inputs
    if "picture" or "Picture" in input:
        url = "https://archive.org/details/" + input
    else:
        print("Input doesn't contain the relevant string. Exiting")
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
    #
    # with urlopen(full_dl_link) as zip_response:
    #     with ZipFile(BytesIO(zip_response.read())) as zfile:
    #         zfile.extractall('./images/%s_jp2' % input)
    #
    # print("Download and extraction complete. Check the images/%s_jp2 subfolder." % input)

# Do the things
# for issue in mag_issues:
#     # Download issue
#     download_mag_issue(issue)
#     # Check if there's an image folder for that issue. Obviously there should be
#     if (os.path.isdir('./images/%s_jp2' % issue)):
#         print("The subfolder %s_jp2 exists!" % issue)
#         # Get into that folder. Actual jp2 folder is down a level and not always the same name :(
#         # Then parse csv. If that issue ID is in column X, copy the file in column y to a new folder.
#     else:
#         print("The subfolder %s_jp2 does NOT exist ... nor should it. Exiting")
#         return

# TESTING ..... #

issue = "Picture-playMagazineJan.1922"
# issue = "pictureplayweekl01unse"
download_mag_issue(issue)
outer_img_path = './images/%s_jp2/' % issue

if not os.path.isdir(outer_img_path): # Does that path/dir exist
    print("The subfolder %s_jp2 does NOT exist ... nor should it. Exiting")
else:
    inner_img_folder = os.listdir(outer_img_path)[0] # Get the folder inside
    path_to_imgs = "%s%s" % (outer_img_path, inner_img_folder)
    # print("JP2s are located in %s" % path_to_imgs)
    # Then parse csv. If that issue ID is in column X, copy the file in column y to a new folder.
    csv_data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
    for row in csv_data:
        vol = row[0]
        no = row[1]
        if row[2] != "":
            day = row[2]
        else:
            day = "day"
        month = row[3]
        year = row[4]
        jp2_img = row[7]
        jp2_filename = jp2_img.split('.')[0]
        for jp2_img in row:
            if "jp2" in jp2_img: # and look by issue
                print("original image is located in", path_to_imgs)
                print("Original image is", jp2_img)
                output_filename = jp2_filename + "_vol" + vol + "_no" + no + "_" + day + "-" + month + "-" + year + ".jp2"
                print("Output filename is", output_filename)
                print("copying ....")
                print("file located at %s/%s" % (path_to_imgs, jp2_img))
                # shutil.copy2("%s/%s" % (path_to_imgs, jp2_img), "./jp2_images/%s" % output_filename)
            # else:
                # print("bzzzz. wrong")
