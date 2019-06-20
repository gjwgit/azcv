Use Case: Extract Programming Code from Photos
==============================================

If all you have is an image of some code but would like to replicate
the code without retyping it all, here's an approach. The following
image (probably from a screenshot) was posted by Emily Klarquist on
[Twitter](https://t.co/kJzwyJg0x0), 20 May 2019. Below is the
extracted code, which is pretty close but not perfect by any means. A
model tuned to extracting code would be more useful here. For now we
need to do some post extraction manual processing. For python code,
for example, we may need to use the bounding box information to guide
indentation.

![](https://pbs.twimg.com/media/D69F90QV4AA9d59.png)
```console
$ ml ocr azcv https://pbs.twimg.com/media/D69F90QV4AA9d59.png
[7, 19, 167, 18, 168, 35, 8, 36] require (ggplot2)
[8, 62, 1118, 61, 1118, 83, 9, 84] nobel_winners <- read. csv ("https://raw. githubusercontent . com/rfordatascience/tidytuesday/master/data/2019/2019-05
[12, 85, 236, 86, 235, 104, 11, 103] -14/nobel_winners . csv")
[6, 146, 1013, 145, 1014, 168, 7, 169] nobel_winners$birth_year <- substring (nobel_winners$birth_date, 1, 4) #pulling year out of the birthdate
[8, 209, 955, 208, 956, 228, 9, 229] nobel_winners$birth_year <- as . integer (nobel_winners$birth_year) #changing birth year to integer
[7, 269, 1034, 268, 1035, 290, 8, 291] nobel_winners$award_age <- (nobel_winners$prize_year - nobel_winners$birth_year) #creating the award age
[10, 330, 771, 329, 772, 351, 11, 352] #ggplot (nobel_winners, aes (x=prize_year, y=award age) ) + #making a basic plot
[30, 356, 158, 355, 159, 372, 31, 373] #geom point ()
[9, 414, 1120, 413, 1120, 434, 10, 436] nobel_winners$category <- ordered (nobel_winners$category, levels = c("Medicine", "Physics", "Chemistry", "Economics"
[13, 437, 503, 437, 502, 457, 12, 456] , "Literature", "Peace") ) #reordering the categories
[9, 459, 303, 460, 302, 481, 8, 479] levels (nobel_winners$category)
[10, 521, 181, 519, 182, 540, 11, 542] ## [1] "Medicine"
[207, 519, 301, 520, 300, 540, 206, 539] "Physics"
[329, 520, 708, 520, 707, 540, 328, 539] "Chemistry" "Economics" "Literature"
[12, 543, 147, 544, 146, 562, 11, 561] ## [6] "Peace"
[6, 605, 1120, 604, 1121, 625, 7, 626] levels (nobel_winners$category) <- c ("Medicine", "Physics", "Chemistry", "Economics*", "Literature", "Peace") #to chang
[10, 628, 155, 629, 154, 648, 9, 647] e facet titles
[12, 688, 798, 689, 797, 711, 11, 710] chart <- ggplot (nobel_winners, aes (x=prize_year, y=award_age, color=category) ) +
[28, 713, 315, 712, 316, 732, 29, 734] geom_point (shape=1, size = 1)
[30, 734, 448, 734, 448, 755, 31, 755] chart + facet_grid (cols = vars (category) ) +
[30, 757, 545, 756, 545, 776, 31, 778] geom_smooth (aes (color=category) , se=FALSE, 1wd=1.5) +
[30, 779, 1118, 780, 1118, 800, 29, 799] labs (title = 'Senescience', subtitle = 'Age of Nobel laureates, at date of award', caption = 'Source: Nobelpri
[11, 804, 74, 805, 74, 824, 10, 822] ze . org
[861, 801, 1120, 801, 1120, 822, 862, 822] * the economics prize was f
[10, 825, 711, 826, 710, 845, 9, 844] irst awarded in 1969' ) + #add titles, not sure how to add two captions
[49, 870, 1120, 869, 1121, 890, 50, 891] theme (plot . title = element_text (face = "bold"), legend. position = "none", strip. text. x = element_text (angle =
[22, 892, 1121, 891, 1122, 912, 23, 913] 0, hjust=0, face="bold", color = c("#014d64", "#90353B", "#EE6A50", "#2D6D66", "#EE9A00", "#01A209") ) ) + #attempt at
[22, 916, 250, 914, 251, 934, 23, 935] changing x facet titles
[53, 937, 779, 938, 779, 959, 52, 958] theme (plot . caption = element_text (hjust = 0, size = 9) ) + #moving caption
[27, 959, 1118, 959, 1119, 980, 28, 980] scale_x_continuous (name= "", breaks= c (1900, 1925, 1950, 1975, 2000) , labels=c (1900, "",50, "", 2000), limits=c (1900, 2
[12, 981, 306, 982, 305, 1003, 11, 1002] 025) ) + #edit x axis and breaks
[33, 1005, 1120, 1004, 1120, 1026, 34, 1027] scale_y_continuous (name="", breaks=c (25, 50, 75, 100) , labels=c (25, 50, 75, 100), position = "right", 25, limits=c(15
[10, 1029, 98, 1027, 98, 1047, 11, 1050] , 101) ) +
[50, 1051, 1092, 1050, 1093, 1071, 51, 1072] theme (panel . grid. major. x = element_blank (), panel. grid. minor. x = element_blank () , ) + #edit y axis and grid
[42, 1073, 1080, 1072, 1081, 1092, 43, 1093] scale_colour_manual (values=c ("#014d64", "#90353B", "#EE6A50", "#2D6066", "#EE9A00", "#01A209") ) + #manual color
[48, 1096, 1106, 1094, 1107, 1116, 49, 1117] annotate ("text", x= Inf, y= 96, label = "Oldest winner \n Leonid Hurwicz, 90", hjust = 1, size = 2.5, colour
[37, 1119, 750, 1117, 751, 1139, 38, 1141] c ("grey92", "grey92", "grey92", "#2D6066", "grey92", "grey92") ) + #add Oldest
[47, 1141, 1117, 1140, 1118, 1161, 48, 1162] annotate ("text", x= Inf, y= 25, label = "Youngest winner \n Malala Yousafzai, 17", hjust = 1, size = 2.5, col
[11, 1163, 779, 1162, 780, 1184, 12, 1185] our = c ("grey92", "grey92", "grey92", "grey92", "grey92", "#01A209") ) #add youngest
```
