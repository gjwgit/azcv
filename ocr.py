# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to extract text from an image.
#
# ml ocr azcv <path>
#
# ml ocr azcv https://azurecomcdn.azureedge.net/cvt-1979217d3d0d31c5c87cbd991bccfee2d184b55eeb4081200012bdaf6a65601a/images/shared/cognitive-services-demos/read-text/read-1-thumbnail.png
# ml ocr azcv http://www.handwrittenocr.com/images/Handwriting/16.jpg
# ml ocr azcv http://www.handwrittenocr.com/images/Handwriting/9.jpg

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import TextRecognitionMode
from azure.cognitiveservices.vision.computervision.models import TextOperationStatusCodes

import os
import sys
import time
import argparse

from mlhub.pkg import azkey, is_url
from mlhub.utils import get_cmd_cwd

# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path or url to image')

option_parser.add_argument(
    '--handwritten',
    action='store_true',
    help='use the handwritten tuned model rather than printed')

args = option_parser.parse_args()

# ----------------------------------------------------------------------

SERVICE   = "Computer Vision"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

# Request subscription key and endpoint from user.

subscription_key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False)

# Set credentials.

credentials = CognitiveServicesCredentials(subscription_key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)

# Check the URL supplied or path exists and is an image.

# Send provided image (url or path) to azure to extract text.

url = args.path

# Choose between handwritten and printed. Default is printed. Use
# --handwritten to use the handwritten model.

if args.handwritten:
    mode = TextRecognitionMode.handwritten
else:
    mode = TextRecognitionMode.printed
raw = True
custom_headers = None
numberOfCharsInOperationId = 36

# Asynchronous call.

if is_url(url):
    rawHttpResponse = client.batch_read_file(url, mode, custom_headers,  raw)
else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        rawHttpResponse = client.batch_read_file_in_stream(fstream, mode, custom_headers, raw)

# Get ID from returned headers.

operationLocation = rawHttpResponse.headers["Operation-Location"]
idLocation = len(operationLocation) - numberOfCharsInOperationId
operationId = operationLocation[idLocation:]

# Get the result.

while True:
    result = client.get_read_operation_result(operationId)
    if result.status not in ['NotStarted', 'Running']:
        break
    time.sleep(1)

# Get data.

if result.status == TextOperationStatusCodes.succeeded:
    for textResult in result.recognition_results:
        for line in textResult.lines:
            print('[{}] {}'.format(", ".join(map(str, line.bounding_box)), line.text))

# Generate locally annotated image

