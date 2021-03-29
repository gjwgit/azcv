# -*- coding: utf-8 -*-
#
# Time-stamp: <Thursday 2020-06-25 10:14:20 AEST Graham Williams>
#
# Copyright (c) Togaware Pty Ltd. All rights reserved.
# Licensed under the MIT License.
#
# A command line to extract text from an image.
#
# ml ocr azcv <path>

import os
import sys
import time
import argparse
import requests

from distutils.version import StrictVersion as ver

from mlhub.pkg import azkey, is_url
from mlhub.utils import get_cmd_cwd

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision import VERSION as azver
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

from msrest.authentication import CognitiveServicesCredentials

# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path or url to image')

args = option_parser.parse_args()

# ----------------------------------------------------------------------

SERVICE   = "Computer Vision"
KEY_FILE  = os.path.join(os.getcwd(), "private.txt")

# Request subscription key and endpoint from user.

key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False)

# Set credentials.

credentials = CognitiveServicesCredentials(key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)
apiver = client.api_version

# Check the URL supplied or path exists and is an image.

# Send provided image (url or path) to azure to extract text.

url = args.path

raw = True
numberOfCharsInOperationId = 36

# Asynchronous call.

if is_url(url):
    request = requests.get(url)
    if request.status_code != 200:
        print(f"The URL does not appear to exist. Please check.")
        print(f"    {url}")
        quit()
    try:
        rawHttpResponse = client.read(url, raw=raw)
    except Exception as e:
        print(f"Error: {e}\n{url}")
        quit()

else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            rawHttpResponse = client.read_in_stream(fstream, raw=raw)
        except Exception as e:
            print(f"Error: {e}\n{path}")
            sys.exit(1)

# Get ID from returned headers.

operationLocation = rawHttpResponse.headers["Operation-Location"]
idLocation = len(operationLocation) - numberOfCharsInOperationId
operationId = operationLocation[idLocation:]

# Get the result.

while True:
    result = client.get_read_result(operationId)
    if result.status not in [OperationStatusCodes.not_started,
                             OperationStatusCodes.running]:
        break
    time.sleep(1)

# Print result.

if result.status == OperationStatusCodes.succeeded:
    for line in result.analyze_result.read_results[0].lines:
        print(f'{" ".join(map(str, line.bounding_box))},{line.text}')

