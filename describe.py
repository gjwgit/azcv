# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to describe an image.
#
# ml describe azcv <path>

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

import os
import argparse
import sys
import urllib.error
import urllib.request

from mlhub.pkg import is_url, get_cmd_cwd,get_private
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

subscription_key, endpoint = get_private()

# Set credentials.

credentials = CognitiveServicesCredentials(subscription_key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)

# Check the URL supplied or path exists and is an image.

# Send provided image (url or path) to azure to extract text.

# ----------------------------------------------------------------------
# URL or path
# ----------------------------------------------------------------------

path = args.path

# ----------------------------------------------------------------------
# Defaults - should be set and changable by argparse - TODO
# ----------------------------------------------------------------------

domain = "landmarks"
language = "en"
max_descriptions = 3

if is_url(path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(path, headers=headers)

        if urllib.request.urlopen(req).status == 200:
            try:
                analysis = client.describe_image(path, max_descriptions, language)
            except Exception as e:
                catch_exception(e, path)

    except urllib.error.URLError:
        sys.exit("Error: The URL does not appear to exist. Please check.\n"
                 f"{path}")

else:
    path = os.path.join(get_cmd_cwd(), path)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.describe_image_in_stream(fstream, max_descriptions, language)
        except Exception as e:
            catch_exception(e, path)

for caption in analysis.captions:
    print("{},{}".format(round(caption.confidence, 2), caption.text))
