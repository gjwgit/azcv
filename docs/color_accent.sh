#!/bin/sh

img=$1
dest=$2

accent="#"$(ml color azcv $1 | cut -d, -f2)

convert -size 100x30 xc: -draw "stroke $accent fill $accent rectangle 30,10 90,20" -gravity North -pointsize 10 -annotate 0 "$accent" \
	color_accent.png

convert $1 color_accent.png -gravity Center +append -bordercolor White -border 10x10 $dest

eom $dest
