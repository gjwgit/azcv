Use Case: Generating Good Thumbnails
====================================

Generating a thumbnail from a photo may sound like a pretty simple
task. However, what should go into the thumbnail to give the most
informative indication of the content of the full photo. This is the
task addressed by the thumbnail service as part of the computer vision
cognitive service.

As a command line tool an input image file is supplied and a thumbnail
image file is created with the same name but with -thumbnail appended
to the file name and saved locally.

![](https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg)
```console
$ ml thumbnail azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
pexels-photo-338515-thumbnail.jpeg
```
![](pexels-photo-338515-thumbnail.jpeg)

![](http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg)
```console
$ ml thumbnail azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
marina_bay_sands_singapore_a_l-thumbnail.jpg
```
![](marina_bay_sands_singapore_a_l-thumbnail.jpg)
