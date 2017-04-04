#!/usr/bin/env bash

echo "Converting jp2s. This will take some time ..."

for img in jp2_images/*.jp2; do
  convert "$img" -resize 300 "${img%.jp2}_sml.jpg";
  # convert "$img" "${img%.jp2}_fullsize.jpg";
  echo "Converted $img"
done

echo "Moving jpgs to the jpg_derivatives folder."
mv jp2_images/*.jpg jpg_derivatives/

echo "Complete!"
