#!/bin/sh

# ml faces azcv faces.jpg > faces_bb.txt

arrow_head="l -15,-5  +5,+5  -5,+5  +15,-5 z"

convert -size 100x30 xc: -draw 'stroke skyblue fill skyblue rectangle 30,14 70,16' \
        -draw "stroke skyblue fill skyblue path 'M 70,15  $arrow_head' " \
	arrow_horizontal.png

cat faces_bb.txt |
  cut -d, -f1 |
  xargs printf '-draw "rectangle %s,%s %s,%s" ' |
  awk '{print "faces.jpg -fill none -stroke blue -strokewidth 3 " $0 "faces_tmp.png"}' |
  xargs convert

# Combine

convert faces.jpg arrow_horizontal.png faces_tmp.png -gravity Center +append -resize 30% -bordercolor White -border 10x10 faces_bb.png

eom faces_bb.png
