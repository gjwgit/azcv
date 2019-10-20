#!/bin/sh

# ml objects azcv objects.jpg > objects_bb.txt

arrow_head="l -15,-5  +5,+5  -5,+5  +15,-5 z"

convert -size 100x30 xc: -draw 'stroke skyblue fill skyblue rectangle 30,14 70,16' \
        -draw "stroke skyblue fill skyblue path 'M 70,15  $arrow_head' " \
	arrow_horizontal.png

cat objects_bb.txt |
  xargs printf '-draw "rectangle %s,%s %s,%s" ' |
  awk '{print "objects.jpg -fill none -stroke blue -strokewidth 3 " $0 "objects_tmp.png"}' |
  xargs convert

# Combine

convert objects.jpg arrow_horizontal.png objects_tmp.png -gravity Center +append -resize 30% -bordercolor White -border 10x10 objects_bb.png

eom objects_bb.png
