#!/usr/bin/env python3
import csv
import os

def write_image_data():
    csv_data = csv.reader(open('./data/pictureplay_data.csv', 'r'))
    new_csv = csv.writer(open('./data/pictureplay_data_imagefiles.csv', 'w'))
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
        jp2_filename = "jp2_images/Picture-Play_vol" + vol + "_no" + no + "_" + day + "-" + month + "-" + year + ".jp2"
        output_filename = "Picture-Play_vol" + vol + "_no" + no + "_" + day + "-" + month + "-" + year + "_sml.png"
        if os.path.isfile(jp2_filename):
            print("%s exists!" % jp2_filename)
            row.append(output_filename)
            new_csv.writerow(row)
        else:
            new_csv.writerow(row)

write_image_data()
