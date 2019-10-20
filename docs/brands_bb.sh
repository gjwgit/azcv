#!/bin/sh

# ml brands azcv gray-shirt-logo.jpg > brands_bb.txt

arrow_head="l -15,-5  +5,+5  -5,+5  +15,-5 z"

convert -size 100x30 xc: -draw 'stroke skyblue fill skyblue rectangle 30,14 70,16' \
        -draw "stroke skyblue fill skyblue path 'M 70,15  $arrow_head' " \
	arrow_horizontal.png

cat brands_bb.txt |
  cut -d',' -f1 |
  xargs printf '-draw "rectangle %s,%s %s,%s" ' |
  awk '{print "gray-shirt-logo.jpg -fill none -stroke blue -strokewidth 3 " $0 "brands_tmp.png"}' |
  xargs convert

# Combine

convert gray-shirt-logo.jpg arrow_horizontal.png brands_tmp.png -gravity Center +append -resize 70% -bordercolor White -border 10x10 brands_bb.png

eom brands_bb.png
