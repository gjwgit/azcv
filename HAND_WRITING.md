Use Case: Reading Handwritten Text
==================================

Here we demonstrate one specific capability of Azure Computer Vision
cognitive service, extracting text from an image of handwritten text,
as exposed through the [MLHub](https://mlhub.ai) package
[azcv](https://github.com/Azure/azcv).

Here are a few examples of handwriting extraction.

![](http://www.handwrittenocr.com/images/Handwriting/16.jpg)

``` console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/16.jpg
237.0 91.0 469.0 92.0 468.0 124.0 236.0 123.0,Education First
188.0 157.0 287.0 158.0 286.0 184.0 187.0 183.0,always
290.0 156.0 424.0 159.0 423.0 184.0 289.0 181.0,dream
426.0 159.0 661.0 154.0 662.0 179.0 427.0 184.0,of a world
32.0 187.0 110.0 189.0 109.0 213.0 31.0 211.0,where
250.0 188.0 293.0 188.0 293.0 209.0 250.0 211.0,see
352.0 185.0 434.0 188.0 433.0 216.0 351.0 213.0,every
458.0 185.0 682.0 184.0 683.0 210.0 459.0 211.0,child , girl or
39.0 216.0 100.0 217.0 99.0 244.0 39.0 242.0,boy,
103.0 214.0 226.0 217.0 226.0 244.0 102.0 240.0,holding
279.0 216.0 356.0 217.0 355.0 240.0 278.0 239.0,books
393.0 213.0 695.0 214.0 694.0 239.0 393.0 239.0,in her/his hands,
37.0 244.0 136.0 246.0 135.0 274.0 36.0 271.0,wearing
204.0 247.0 298.0 248.0 297.0 270.0 203.0 269.0,school
305.0 245.0 675.0 243.0 676.0 271.0 306.0 272.0,uniform and going to
33.0 277.0 169.0 271.0 171.0 296.0 34.0 301.0,School : g
221.0 276.0 295.0 274.0 296.0 297.0 222.0 299.0,will
301.0 274.0 676.0 272.0 677.0 297.0 302.0 299.0,struggle to make this
41.0 304.0 631.0 302.0 632.0 329.0 42.0 331.0,today's dream , tomorrow's reality. 9
31.0 334.0 260.0 333.0 261.0 359.0 32.0 360.0,always believe
269.0 333.0 673.0 332.0 674.0 358.0 270.0 359.0,that even one look ,
35.0 365.0 666.0 362.0 667.0 387.0 36.0 390.0,one pen , one child , one teacher can
33.0 395.0 122.0 394.0 123.0 417.0 34.0 418.0,change
180.0 394.0 223.0 394.0 222.0 417.0 180.0 416.0,the
224.0 390.0 359.0 391.0 358.0 418.0 223.0 416.0,world .
443.0 416.0 682.0 422.0 681.0 450.0 442.0 444.0,malala yousafzai
```
![](http://www.handwrittenocr.com/images/Handwriting/1.jpg)
```console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/1.jpg
274.0 141.0 507.0 102.0 520.0 198.0 299.0 240.0,if the
143.0 276.0 603.0 254.0 606.0 318.0 146.0 340.0,only prayer
108.0 411.0 587.0 371.0 593.0 438.0 114.0 479.0,you said was
149.0 522.0 569.0 516.0 570.0 588.0 150.0 594.0,thank you,
84.0 663.0 606.0 644.0 609.0 716.0 87.0 735.0,that would be
185.0 795.0 503.0 778.0 506.0 848.0 189.0 866.0,enough.
498.0 898.0 606.0 871.0 615.0 910.0 507.0 937.0,master
537.0 927.0 619.0 907.0 629.0 942.0 545.0 963.0,copart
```

![](http://www.handwrittenocr.com/images/Handwriting/9.jpg)

```console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/9.jpg
6.0 45.0 549.0 35.0 550.0 65.0 7.0 75.0,Reading a handwritten article about hand .
4.0 86.0 549.0 78.0 550.0 109.0 5.0 117.0,writing , in a 215-century magazine, is like
6.0 132.0 527.0 123.0 527.0 150.0 7.0 160.0,listening to your great-great- grandfather
6.0 175.0 542.0 163.0 543.0 193.0 7.0 206.0,shout in the middle of a crowded multiplex
8.0 217.0 550.0 207.0 551.0 237.0 9.0 248.0,about the incomparable glories of vaudeville
7.0 259.0 545.0 249.0 546.0 277.0 8.0 287.0,and the lost art of wearing hats in public.
8.0 300.0 557.0 287.0 558.0 313.0 9.0 325.0,And yet, somehow, here we are . Certain vestigial
```

