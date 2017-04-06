### mhdl-scripts

Scripts for working with media history magazines from the [Media History Digital Library](http://mediahistoryproject.org/), hosted on the internet archive.  
This series of scripts downloads all issues of a particular magazine, extracts the zip files, copies the magazine cover images (JPEG2000), and converts these images to JPEG.  
This process uses data that has been collected on volume IDs, the cover filenames, the link to that page in the book reader, etc. At the end, a new CSV is output which adds the names of the jpeg derivatives to the existing data.

#### Dependencies

* `imagemagick` - command line image manipulation program.
* `BeautifulSoup` - Python library for parsing HTML.

#### How to use

Instructions [here](./dev_notes.md).

#### ⚠ Note

This is a proof-of-concept type thing, scripts currently work for gaining the images for _Picture Play_ magazine.  
However, could quite easily be amended to work for other titles.

##### Questions

* Is it possible download only selected files from a zip file? It doesn't seem that there is, but this would be great - it's very lengthy and disk heavy to download all of the zip files.
