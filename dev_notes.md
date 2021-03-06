### How to use these scripts

1. Create subfolders:
   * `mkdir issue_downloads jp2_images jpg_derivatives`.

2. `download_mag_volumes.py` downloads and unzips the folder of jp2 images for each volume.   
   * `python3 download_mag_volumes.py`   

3. `grab_mag_covers.py` copies just the cover images to <i>jp2_images</i>.
   * `python3 grab_mag_covers.py`

4. `jp2_to_jpg.sh` converts the jp2s to jpgs and resizes them to 300w, then moves them to the folder <i>jpg_derivatives</i>.
   * `chmod +x jp2_to_jpg.sh`
   * `./jp2_to_jpg.sh`  

5. `write_image_data.py` writes the jpg filename into the CSV data file `data/picture_data_imagefiles.csv`.
   * `python3 write_image_data.py`  

Suggested:

6. Check `picture_data_imagefiles.csv` for gaps where there shouldn't be.

7. Cleanup - if everything looks good, delete the contents of <i>image_downloads</i>: `rm -rf issue_downloads/*`.

_**Note on data**_: there are some mag issues that appear in the listing twice, because two scanned volumes hosted on archive.org include them (e.g., _Picture Play_ vol. 18). The same derivative image is referenced to each, because the image file gets saved over when it hits the second listing.
