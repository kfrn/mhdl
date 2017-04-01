#!/usr/bin/env python3
import shutil
import os

from get_issue_list import get_issue_list

def does_imgfolder_exist(img_path):
    return os.path.isdir(img_path)

def get_path_to_imgs(outer_folder):
    return outer_folder + os.listdir(outer_folder)[0]

def copyRelImageFiles(input):
    outer_img_folder = './issue_downloads/%s_jp2/' % input

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
            day = "dd"
        month = row[3]
        year = row[4]
        book_id = row[6]
        jp2_img = row[7]
        output_filename = "Picture-Play_vol" + vol + "_no" + no + "_" + day + "-" + month + "-" + year + ".jp2"
        if book_id == input:
            # Account for cases where there is no book cover
            # TODO!: account for blanks in the jp2_img field.
            if not "picture" in jp2_img.lower():
                print("Book id is %s and filename field contains: %s" % (book_id, jp2_img))
                return
            else:
                shutil.copy2("%s/%s" % (path_to_imgs, jp2_img), "./jp2_images/%s" % output_filename)
                print("Output file created in the jp2_images directory:", output_filename)

mag_issues = get_issue_list()
# print(mag_issues)

# for issue in mag_issues:
#     copyRelImageFiles(issue)
