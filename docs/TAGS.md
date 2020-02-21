Identifying Landmarks and Tags
==============================

Here we demonstrate one specific capability of Azure Computer Vision
cognitive service, tagging photos, as exposed through the
[MLHub](https://mlhub.ai) package
[azcv](https://github.com/gjwgit/azcv).

Here are a few examples of identifying landmarks and tagging
images.

A key benefit from using command line tools is that each task can be
wrapped up into other pipelines. Simply place a shell for loop around
the command and we can operate on a folder of images or indeed, a disk
of images.

*ToDo* Some command line use cases in the pipeline include analysing a
photo to add tags and the primary landmarks as meta-data to the image
itself.

![](https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg)

```console
$ ml landmarks azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
0.97,Eiffel Tower

$ ml tags azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
1.00,sky
0.99,outdoor
0.98,tower
0.94,cloud
0.80,city
0.79,skyscraper

$ ml describe azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
0.71,a large clock tower towering over Eiffel Tower
0.66,a large clock tower towering over the city of london with Eiffel Tower in the background
0.66,the tower of the city with Eiffel Tower in the background
```
![](http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg)
```console
$ ml landmarks azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
0.97,Marina Bay Sands

$ ml tags azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
0.99,sky
0.99,ship
0.99,water
0.96,skyscraper
0.95,outdoor
0.95,scene
0.94,boat
0.89,harbor
0.85,lake
0.77,bridge
0.74,city
0.69,watercraft
0.67,building
0.51,dock
0.40,docked

$ ml describe azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
0.65,a boat is docked next to a body of water with Marina Bay Sands in the background
0.65,a large body of water with Marina Bay Sands in the background
0.65,a boat docked next to a body of water with Marina Bay Sands in the background
```
![](https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg)
```console
$ ml landmarks azcv https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg
1.0,Uluru

$ ml tags azcv https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg
1.00,sky
1.00,outdoor
1.00,sunset
0.99,grass
0.99,mountain
0.99,nature
0.96,landscape
0.94,cloud
0.94,plant
0.93,canyon
0.88,valley
0.86,desert
0.82,setting
0.75,clouds
0.71,sunrise
0.70,background
0.49,tall
0.35,overlooking
0.23,painting

$ ml describe azcv https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg
0.92,a canyon with a sunset in the background with Uluru in the background
0.88,a view of a canyon with a sunset in the background with Uluru in the background
0.86,a close up of a canyon with a sunset in the background with Uluru in the background
```
![](https://access.togaware.com/landmark02.jpg)
```console
$ ml landmarks azcv https://access.togaware.com/landmark02.jpg
0.98,Taipei 101

$ ml tags azcv https://access.togaware.com/landmark02.jpg
1.00,building
0.99,outdoor
0.99,sky
0.85,city
0.74,window
0.57,skyscraper
0.55,architecture
0.51,tall

$ ml describe azcv https://access.togaware.com/landmark02.jpg
0.92,a large skyscraper in front of Taipei 101
0.92,a large skyscraper in front of a tall building with Taipei 101 in the background
0.92,a tall building with Taipei 101 in the background
```
![](https://access.togaware.com/landmark01.jpg)
```console
$ ml landmarks azcv https://access.togaware.com/landmark01.jpg
1.0,Borobudur
```
![](https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg)
```console
$ ml landmarks azcv https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg
0.96,Ha Long Bay
```

*How Many Tags Identified in an Image*

```console
$ ml tags azcv img.jpg | wc -l
6
```
*How Many High Confidence Tags Identified*

```console
$ ml tags azcv img.jpg | awk '$1 > 0.90 {print}' | wc -l
5
```

*Identify Tags from a Folder of Images*

```console
$ for f in *.jpg; do echo ==== $f ====; ml tags azcv $f; done
==== 20190610_133243.jpg ====
1.00,indoor
0.99,furniture
0.95,bathroom
0.90,design
0.75,sink
0.61,drawer
0.60,home appliance
==== 20190610_143537.jpg ====
0.94,screenshot
0.92,book
0.91,poster
0.88,indoor
0.63,art
0.59,mobile phone
[...]
```

