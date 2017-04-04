### mhdl-scripts

Scripts for working with media history magazines from the [Media History Digital Library](http://mediahistoryproject.org/), hosted on the internet archive.  
This series of scripts downloads all issues of a particular magazine, extracts the zip files, copies from each all of the jp2 images that correspond to a magazine cover, and converts these images to jp2.  
This process is reliant on CSV data supplied, which gives the cover filenames etc. At the end, a new CSV is output which also lists the names of the jpeg derivatives.

#### Dependencies

`imagemagick` - command line image manipulation program.
`BeautifulSoup` - Python library for parsing HTML.

#### How to use

Instructions [here](./dev_notes.md).

##### Thinking out loud ...

* Is it possible download only selected files from a zip file? It doesn't seem that there is, but this would be great - very lengthy and disk heavy to download all of the volume zip files. 
