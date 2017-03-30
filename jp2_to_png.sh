#!/usr/bin/env bash

echo "Converting jp2s. This will take some time ..."

for img in jp2_images/*.jp2; do
  convert "$img" -resize 300 "${img%.jp2}_sml.png";
  convert "$img" "${img%.jp2}_fullsize.png";
  echo "Converted $img"
done

echo "Moving pngs to the png_derivatives folder."
mv jp2_images/*png png_derivatives/

echo "Complete!"
