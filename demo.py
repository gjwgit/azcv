# -*- coding: utf-8 -*-
#
# Time-stamp: <Thursday 2020-06-25 09:48:23 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# ml demo azcv
#
# This demo is based on the Quick Start.
#
# https://pypi.org/project/azure-cognitiveservices-vision-computervision

from mlhub.pkg import mlask, mlcat, mlpreview
from mlhub.utils import get_private

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
import io    # Create local image.
import sys
import time

from distutils.version import StrictVersion as ver
from textwrap import fill
from PIL import Image

# pip3 install azure-cognitiveservices-vision-computervision

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision import VERSION as azver
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

from msrest.authentication import CognitiveServicesCredentials

if ver(azver) < ver("0.6.0"):
    sys.exit(f"""*** WARNING *** Currently you have installed version {azver} of the
Azure Cognitives Services Computer Vision library. This might have
been installed automatically as part of the *configure* of the
package. Some incompatible changes have emerged in recent
upgrades. Please upgrade to the latest version of that library using:

    pip3 install --upgrade azure-cognitiveservices-vision-computervision
""")
    
# ----------------------------------------------------------------------
# Request subscription key and location from user.
# ----------------------------------------------------------------------

PRIVATE_FILE = "private.json"

path = os.path.join(os.getcwd(), PRIVATE_FILE)

private_dic = get_private(path, "azcv")

if "key" not in private_dic["Computer Vision"]:
    print("There is no key in private.json. Please run ml configure azcv to upload your key.", file=sys.stderr)
    sys.exit(1)

key = private_dic["Computer Vision"]["key"]

endpoint = private_dic["Computer Vision"]["endpoint"]

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

try:
    image_analysis = client.analyze_image(url, visual_features=[VisualFeatureTypes.tags])
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Please run ml configure azcv to update your private information.", file=sys.stderr)
    quit()

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

try:
    analysis = client.analyze_image_by_domain(domain, url, language)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Please run ml configure azcv to update your private information.", file=sys.stderr)
    quit()

mlask()

for landmark in analysis.result["landmarks"]:
    print('\nIdentified "{}" with confidence {}.'.format(landmark["name"], round(landmark["confidence"],2)))

mlask(begin="\n", end="\n")

url1 = "https://cdn.britannica.com/"
url2 = "95/94195-050-FCBF777E/"
url3 = "Golden-Gate-Bridge-San-Francisco.jpg"
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

try:
    analysis = client.describe_image(url, max_descriptions, language)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Please run ml configure azcv to update your private information.", file=sys.stderr)
    quit()

mlask(end="\n")

for caption in analysis.captions:
    print(fill("With confidence of {} found {}".format(round(caption.confidence, 2), caption.text)) + "\n")

# Image to Text Example
    
mlask()

url1 = "https://azurecomcdn.azureedge.net/"
url2 = "cvt-1979217d3d0d31c5c87cbd991bccfee2d184b55eeb4081200012bdaf6a65601a/"
url3 = "images/shared/cognitive-services-demos/read-text/read-1-thumbnail.png"
url = url1 + url2 + url3
# The following has disappeared.
url = "http://www.handwrittenocr.com/images/Handwriting/16.jpg"
url = "https://github.com/gjwgit/azcv/raw/master/images/mycat.png"

mlcat("Text From Image",
f"""We now identify text from an imag. The results include the bounding
box coordinates for the text as well as the text itself. Piping the
output to other commands allows the image itself to be marked up with
the identified text. See the *ocr* command to utilise this
functionality as a command line tool for extracting text from any
supplied image.

For our demonstration we will analyze the following image which we will also 
display momentarily:

  {url}""", begin="\n")

mlpreview(url)

# This requires two calls using batch_read_file() and
# get_read_operation_result(). The call to batch_read_file() is
# asynchronous. In the results of the call to
# get_read_operation_result(), we need to check if the first call
# completed with OperationStatusCodes before extracting the text
# data. The results include the text as well as the bounding box
# coordinates for the text.

raw = True
numberOfCharsInOperationId = 36

# Asynchronous call.
try:
    rawHttpResponse = client.read(url, raw=raw)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Please run ml configure azcv to update your private information.", file=sys.stderr)
    quit()

# Get ID from returned headers.

operationLocation = rawHttpResponse.headers["Operation-Location"]
idLocation = len(operationLocation) - numberOfCharsInOperationId
operationId = operationLocation[idLocation:]

# Wait for the result.

while True:
    result = client.get_read_result(operationId)
    if result.status not in [OperationStatusCodes.not_started,
                             OperationStatusCodes.running]:
        break
    time.sleep(1)

mlask(end="\n")
    
# Print the results.

if result.status == OperationStatusCodes.succeeded:
    for line in result.analyze_result.read_results[0].lines:
        print(f'Found "{line.text}"\n  at [{", ".join(map(str, line.bounding_box))}]\n')
            
mlask()

url = "https://cdn.britannica.com/95/94195-050-FCBF777E/Golden-Gate-Bridge-San-Francisco.jpg"

mlcat("Generate Good Thumbnails",
"""A utility provided by the service can generate a thumbnail (JPG) of an image. 
The thumbnail does not need to be in the same proportions as the original
image and indeed we will often want to create square thumbnails. In creating a
thumbnail though we also want to capture the most interesting part of the image.
This service will create such a thumbnail. Here we create a square 100x100
thumbnail.

For our demonstration we will analyze the following image which we will also 
display momentarily:

URL:{}""".format(url), begin="\n")

mlpreview(url)

# 100 below results in error.

width = 50 
height = 50

try:
    thumbnail = client.generate_thumbnail(width, height, url)
except Exception as e:
    print(f"Error: {e}", file=sys.stderr)
    print("Please run ml configure azcv to update your private information.", file=sys.stderr)
    quit()

for x in thumbnail:
    image = Image.open(io.BytesIO(x))

image.save('thumbnail.jpg')

mlask()
mlpreview('thumbnail.jpg')
