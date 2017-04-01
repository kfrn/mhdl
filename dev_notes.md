### Notes

To get all the issue covers:

1. Create these folders: `issue_downloads`, `jp2_images`, and `png_derivatives`.

2. `download_cover_images.py` downloads the file of images (jp2) for each issue, extracts the folder, and copies just the issue cover images to <i>jp2_images</i>.
  * `python3 download_cover_images.py`   

3. `jp2_to_png.sh` converts the jp2s to pngs and resizes them to 300w. Then moves them to the folder <i>png_derivatives</i>.
  * `chmod +x jp2_to_png.sh`
  * `./jp2_to_png.sh`  

4. `write_image_data.py` writes the png filename into the CSV data file `data/picture_data_imagefiles.csv`.
  * `python3 write_image_data.py`  


_Note on data_: there are some mag issues that appear in the listing twice, because two scanned volumes include them (e.g., _Picture Play_ vol. 18). Only one image is created because it gets saved over when it hits the second listing. 

This is a proof-of-concept and just targets one specific magazine, _Picture Play_.
