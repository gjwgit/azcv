Use Case: Reading Street Signs
==============================

Extracting text from photos becomes more important in the context of
autonomous vehicles where street signs may play an important role. The
challenge for this task is to not only extract text from the image,
but to identify the text that was on a street sign. Text otherwise can
be found in many locations within a photo. In the examples below we do
not yet consider that task of limiting the text extration to the
street signs.

![](https://sharpie51.files.wordpress.com/2010/02/street_sign_for_abbey_road_in_westminster_london_england_img_1461.jpg)

```console
$ ml ocr azcv https://sharpie51.files.wordpress.com/2010/02/street_sign_for_abbey_road_in_westminster_london_england_img_1461.jpg
325 305 1297 290 1302 594 329 609,ABBEY
311 664 1937 652 1940 943 314 955,ROAD NW8
343 1142 1784 1121 1786 1253 345 1273,CITY OF WESTMINSTER
```
![](https://farm4.staticflickr.com/3883/15144849957_f326e03f75_b.jpg)
```console
$ ml ocr azcv https://farm4.staticflickr.com/3883/15144849957_f326e03f75_b.jpg
341 122 606 120 607 158 342 160,SEMARANG
251 200 559 199 560 237 252 238,PURWODADI
251 250 456 249 456 288 252 289,BLORA
810 510 1022 508 1023 528 811 530,RAHAYU SANTOSA
714 541 1014 538 1014 586 715 590,PARIWIS
90 610 213 609 214 626 91 627,PENERIMAAN PESERTA DIDIK
99 629 204 627 205 638 99 640,Tahun Ajaran 2014 2015
91 666 170 662 171 673 92 678,EXNIX TENAGA LISTRIN
```
![](http://brombeer.net/signs/id_approach.jpg)
```console
$ ml ocr azcv http://brombeer.net/signs/id_approach.jpg
148 84 207 83 208 97 148 98,KELUAR
221 85 246 84 246 99 221 99,07
148 132 328 133 327 160 147 159,R Kembangan
480 133 589 138 587 164 478 159,Serpong
179 161 277 164 276 189 178 186,Meruya
179 190 349 192 348 216 179 215,Duri Kosambi
234 223 293 224 293 245 234 244,1 km
728 367 760 371 756 409 724 405,R
```
![](https://upload.wikimedia.org/wikipedia/commons/7/7e/Indonesian_Road_Sign_-_NR_Directional.png)
```console
$ ml ocr azcv https://upload.wikimedia.org/wikipedia/commons/7/7e/Indonesian_Road_Sign_-_NR_Directional.png
351 90 1272 87 1273 202 352 204,Purwokerto
102 348 209 347 209 367 103 369,NASIONAL
354 397 1273 382 1275 497 356 512,Yogyakarta
353 644 1056 656 1054 761 351 748,Kebumen
1331 703 1436 703 1436 723 1332 724,NASIONAL
356 802 1088 811 1086 946 354 937,Magelang
1340 747 1404 745 1410 832 1346 834,3
```
