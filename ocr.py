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

from mlhub.pkg import is_url, get_cmd_cwd, get_private

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import OperationStatusCodes

from msrest.authentication import CognitiveServicesCredentials
from utils import catch_exception

# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path or url to image')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

key, endpoint = get_private()

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
        sys.exit("The URL does not appear to exist. Please check.\n"
                 f"{url}")
    try:
        rawHttpResponse = client.read(url, raw=raw)
    except Exception as e:
        catch_exception(e, url)

else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            rawHttpResponse = client.read_in_stream(fstream, raw=raw)
        except Exception as e:
            catch_exception(e, path)

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

