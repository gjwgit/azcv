#!/bin/sh

url=$1

wget --quiet --output-document=img.jpg $1
ml ocr azcv img.jpg >| img_bb.txt

# Add bounding boxes to the image.

cat img_bb.txt |
  cut -d',' -f1 |
  xargs printf '-draw "polygon %s,%s %s,%s %s,%s %s,%s" ' |
  awk '{print "img.jpg -fill none -stroke red -strokewidth 5 " $0 "img_bb.jpg"}' |
  xargs convert

# Add the identified text to the image.

cat img_bb.txt |
  tr ',' ' '| 
  cut -d' ' -f1,2,9- | 
  perl -pe 's|([\d\.]+) ([\d\.]+) (.+)|-annotate +\1+\2 \\"\3\\"|' | 
  xargs | 
  awk '{print "img_bb.jpg -stroke white -pointsize 30 " $0 " img_bb_text.jpg"}' | 
  xargs convert

# Create a montage of the original and final image.

montage -background '#336699' -geometry +4+4 img.jpg img_bb_text.jpg montage.jpg

# Display the image.

eog montage.jpg

# Cleanup

# rm img.jpg img_bb.txt img_bb.jpg img_bb_text.jpg
