Use Case: Reading Handwritten Text
==================================

Here are a few examples of handwriting extraction.

![](http://www.handwrittenocr.com/images/Handwriting/16.jpg)

``` console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/16.jpg
[237, 91, 469, 92, 468, 124, 236, 123] Education First
[188, 157, 287, 158, 286, 184, 187, 183] always
[290, 156, 424, 159, 423, 184, 289, 181] dream
[426, 159, 661, 154, 662, 179, 427, 184] of a world
[32, 187, 110, 189, 109, 213, 31, 211] where
[250, 188, 293, 188, 293, 209, 250, 211] see
[352, 185, 434, 188, 433, 216, 351, 213] every
[458, 185, 682, 184, 683, 210, 459, 211] child , girl or
[39, 216, 100, 217, 99, 244, 39, 242] boy,
[103, 214, 226, 217, 226, 244, 102, 240] holding
[279, 216, 356, 217, 355, 240, 278, 239] books
[393, 213, 695, 214, 694, 239, 393, 239] in her/his hands,
[37, 244, 136, 246, 135, 274, 36, 271] wearing
[204, 247, 298, 248, 297, 270, 203, 269] school
[305, 245, 675, 243, 676, 271, 306, 272] uniform and going to
[33, 277, 169, 271, 171, 296, 34, 301] School : g
[221, 276, 295, 274, 296, 297, 222, 299] will
[301, 274, 676, 272, 677, 297, 302, 299] struggle to make this
[41, 304, 631, 302, 632, 329, 42, 331] today's dream , tomorrow's reality. 9
[31, 334, 260, 333, 261, 359, 32, 360] always believe
[269, 333, 673, 332, 674, 358, 270, 359] that even one look ,
[35, 365, 666, 362, 667, 387, 36, 390] one pen , one child , one teacher can
[33, 395, 122, 394, 123, 417, 34, 418] change
[180, 394, 223, 394, 222, 417, 180, 416] the
[224, 390, 359, 391, 358, 418, 223, 416] world .
[443, 416, 682, 422, 681, 450, 442, 444] malala yousafzai
```
![](http://www.handwrittenocr.com/images/Handwriting/1.jpg)
```console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/1.jpg
[274, 141, 507, 102, 520, 198, 299, 240] if the
[143, 276, 603, 254, 606, 318, 146, 340] only prayer
[108, 411, 587, 371, 593, 438, 114, 479] you said was
[149, 522, 569, 516, 570, 588, 150, 594] thank you,
[84, 663, 606, 644, 609, 716, 87, 735] that would be
[185, 795, 503, 778, 506, 848, 189, 866] enough.
[498, 898, 606, 871, 615, 910, 507, 937] master
[537, 927, 619, 907, 629, 942, 545, 963] copart
```

![](http://www.handwrittenocr.com/images/Handwriting/9.jpg)

```console
$ ml ocr azcv --handwritten http://www.handwrittenocr.com/images/Handwriting/9.jpg
[6, 45, 549, 35, 550, 65, 7, 75] Reading a handwritten article about hand .
[4, 86, 549, 78, 550, 109, 5, 117] writing , in a 215-century magazine, is like
[6, 132, 527, 123, 527, 150, 7, 160] listening to your great-great- grandfather
[6, 175, 542, 163, 543, 193, 7, 206] shout in the middle of a crowded multiplex
[8, 217, 550, 207, 551, 237, 9, 248] about the incomparable glories of vaudeville
[7, 259, 545, 249, 546, 277, 8, 287] and the lost art of wearing hats in public.
[8, 300, 557, 287, 558, 313, 9, 325] And yet, somehow, here we are. Certain vestigial
```

