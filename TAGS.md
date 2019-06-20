Identifying Landmarks and Tags
==============================

Here are a few examples of identifying landmarks and tagging the images:

![](https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg)

```console
$ ml landmark azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
0.97 Eiffel Tower

$ ml tag azcv https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
1.00 sky
0.99 outdoor
0.98 tower
0.94 cloud
0.80 city
0.79 skyscraper
```
![](http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg)
```console
$ ml landmark azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
0.97 Marina Bay Sands

$ ml tag azcv http://cdn1.thr.com/sites/default/files/2013/11/marina_bay_sands_singapore_a_l.jpg
0.99 sky
0.99 ship
0.99 water
0.96 skyscraper
0.95 outdoor
0.95 scene
0.94 boat
0.89 harbor
0.85 lake
0.77 bridge
0.74 city
0.69 watercraft
0.67 building
0.51 dock
0.40 docked
```
![](https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg)
```console
$ ml landmark azcv https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg
1.0 Uluru

$ ml tag azcv https://www.wayoutback.com.au/assets/Uploads/Uluru.jpg
1.00 sky
1.00 outdoor
1.00 sunset
0.99 grass
0.99 mountain
0.99 nature
0.96 landscape
0.94 cloud
0.94 plant
0.93 canyon
0.88 valley
0.86 desert
0.82 setting
0.75 clouds
0.71 sunrise
0.70 background
0.49 tall
0.35 overlooking
0.23 painting
```
![](https://access.togaware.com/landmark02.jpg)
```console
$ ml landmark azcv https://access.togaware.com/landmark02.jpg
0.98 Taipei 101
```
![](https://access.togaware.com/landmark01.jpg)
```console
$ ml landmark azcv https://access.togaware.com/landmark01.jpg
1.0 Borobudur
```
![](https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg)
```console
$ ml landmark azcv https://www.arrivalguides.com/s3/ag-images-eu/18/20870ca6f7bc086749ea747ec0c8c86d.jpg
0.96 Ha Long Bay
```

