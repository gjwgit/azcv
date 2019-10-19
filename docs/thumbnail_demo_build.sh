#!/bin/sh

if [ "$#" -ne 3 ]; then
  echo "Three parameters are required: orig.png thumb.png dest.png"
  exit
fi

orig=$1
thumb=$2
dest=$3

arrow_head="l -15,-5  +5,+5  -5,+5  +15,-5 z"

convert -size 100x30 xc: -draw 'stroke skyblue fill skyblue rectangle 30,14 70,16' \
        -draw "stroke skyblue fill skyblue path 'M 70,15  $arrow_head' " \
	arrow_horizontal.png

# eom arrow_horizontal.png

convert ${orig} -resize 400x400 arrow_horizontal.png ${thumb} -gravity Center +append -resize 70% -bordercolor White -border 10x10 ${dest}

eom ${dest}
