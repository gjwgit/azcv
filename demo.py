# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# This demo is based on the Quick Start published on Azure.
#
# https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk

from mlhub.pkg import azkey, azrequest, mlask, mlcat, mlpreview

mlcat("Azure Computer Vision API", """\
Welcome to a demo of pre-built models for Computer Vision available as 
Cognitive Services on Azure.  Azure supports various operations related to
Computer Vision and this package demonstrates them and provides command line
tools for specific tasks, including tag, describe, landmark, ocr, and
thumbnail.
""")

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import os
import io 			# Create local image.
import time

from textwrap import fill
from PIL import Image

# pip3 install azure-cognitiveservices-vision-computervision

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision import VERSION as azver
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

SERVICE   = "Computer Vision"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

key, endpoint = azkey(KEY_FILE, SERVICE)

mlask()

# Set credentials.

credentials = CognitiveServicesCredentials(key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)

url0 = "https://upload.wikimedia.org/"
url1 = "wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/"
url2 = "450px-Broadway_and_Times_Square_by_night.jpg"
url  = url0 + url1 + url2

mlcat("Analyze an image",
"""We can analyze an image for certain features with analyze_image(). We use the
visual_features= property to set the types of analysis to perform on the image. 
Common values are VisualFeatureTypes.tags and VisualFeatureTypes.description. 

For our demonstration we will analyze the following image which we will also 
display momentarily:

Location: {}
Path:     {}
Filename: {}""".format(url0, url1, url2), begin="\n")

mlpreview(url)
mlask(end="\n")

mlcat("Tag Analysis",
"""We list the tags for the image together with a measure of confidence.
""") 

image_analysis = client.analyze_image(url, visual_features=[VisualFeatureTypes.tags])

for tag in image_analysis.tags:
    if tag.confidence > 0.2:
        print("Confidence: {:4.2f} Tag: {}".format(round(tag.confidence, 2), tag.name))

mlask(begin="\n", end="\n")
mlcat("Subject Domain List",
"""Various subject domains can be used to analyze images. The domains include
celebrities and landmarks.
""")
  
models = client.list_models()

for x in models.models_property:
    print(fill(x.name + ": " + ', '.join(x.categories), subsequent_indent="    ") + "\n")

mlask(end="\n")

# Public domain image of Eiffel tower.

url = "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg"

mlcat("Analyze an Image by Domain",
"""We can specify a subject domain within which to analyze an image. For example,
below we use the landmarks domain to identify the landmark in an image. See the
landmark command for a command line tool to identify the landmark in a local or
remote image file.

For our demonstration we will analyze the following image which we will also 
display momentarily.

Location: {}""".format(url))

# Type of prediction.

domain = "landmarks"

mlpreview(url)

# English language response.

language = "en"

analysis = client.analyze_image_by_domain(domain, url, language)

mlask()

for landmark in analysis.result["landmarks"]:
    print('\nIdentified "{}" with confidence {}.'.format(landmark["name"], round(landmark["confidence"],2)))

mlask(begin="\n", end="\n")

url1 = "http://www.public-domain-photos.com/"
url2 = "free-stock-photos-4/travel/san-francisco/"
url3 = "golden-gate-bridge-in-san-francisco.jpg"
url  = url1 + url2 + url3

mlcat("Text Description of an Image",
"""We can obtain a language-based text description of an image and can request
several descriptions for our further text analysis for keywords associated
with the image. 

For our demonstration we will analyze the following image which we will also 
display momentarily:

Location: {}
Path:     {}
Filename: {}""".format(url1, url2, url3))

domain = "landmarks"
language = "en"
max_descriptions = 3

mlpreview(url)

analysis = client.describe_image(url, max_descriptions, language)

mlask(end="\n")

for caption in analysis.captions:
    print(fill("With confidence of {} found {}".format(round(caption.confidence, 2), caption.text)) + "\n")

# Image to Text Example
    
mlask()

url1 = "https://azurecomcdn.azureedge.net/"
url2 = "cvt-1979217d3d0d31c5c87cbd991bccfee2d184b55eeb4081200012bdaf6a65601a/"
url3 = "images/shared/cognitive-services-demos/read-text/read-1-thumbnail.png"
url = url1 + url2 + url3
url = "http://www.handwrittenocr.com/images/Handwriting/16.jpg"

mlcat("Text From Image",
"""We can identify text from an image using Text Recognition Mode. This mode 
supports both handwritten and typed text. The results include the text as well
as the bounding box coordinates for the text so that the image itself can be
marked up with the identified text. See the ocr command to utilise this
functionality as a command line tool for extracting text from any supplied
image.

For our demonstration we will analyze the following image which we will also 
display momentarily:

  {}""".format(url), begin="\n")

mlpreview(url)

# This requires two calls using batch_read_file() and
# get_read_operation_result(). The call to batch_read_file() is
# asynchronous. In the results of the call to
# get_read_operation_result(), we need to check if the first call
# completed with TextOperationStatusCodes before extracting the text
# data. The results include the text as well as the bounding box
# coordinates for the text.

mode = TextRecognitionMode.handwritten
raw = True
custom_headers = None
numberOfCharsInOperationId = 36

# Async SDK call
if ver(azver) > ver("0.3.0"):
    rawHttpResponse = client.batch_read_file(url, custom_headers,  raw)
else:
    rawHttpResponse = client.batch_read_file(url, mode, custom_headers,  raw)

# Get ID from returned headers
operationLocation = rawHttpResponse.headers["Operation-Location"]
idLocation = len(operationLocation) - numberOfCharsInOperationId
operationId = operationLocation[idLocation:]

# SDK call
while True:
    result = client.get_read_operation_result(operationId)
    if result.status not in ['NotStarted', 'Running']:
        break
    time.sleep(1)

mlask(end="\n")
    
# Get data.

if result.status == TextOperationStatusCodes.succeeded:
    for textResult in result.recognition_results:
        for line in textResult.lines:
            print('Found "{}" at [{}]\n'.format(line.text, ", ".join(map(str, line.bounding_box))))

            
mlask()

url1 = "http://www.public-domain-photos.com/free-stock-photos-4/"
url2 = "travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg"
url  = url1 + url2

mlcat("Generate Interesting Thumbnail",
"""A utility provided by the service can generate a thumbnail (JPG) of an image. 
The thumbnail does not need to be in the same proportions as the original
image and indeed we will often want to create square thumbnails. In creating a
thumbnail though we also want to capture the most interesting part of the image.
This service will create such a thumbnail. Here we create a square 100x100
thumbnail.

For our demonstration we will analyze the following image which we will also 
display momentarily:

Site: {}
Path: {}""".format(url1, url2), begin="\n")

mlpreview(url)

# 100 below results in error.

width = 50 
height = 50

thumbnail = client.generate_thumbnail(width, height, url)

for x in thumbnail:
    image = Image.open(io.BytesIO(x))

image.save('thumbnail.jpg')

mlask()
mlpreview('thumbnail.jpg')
