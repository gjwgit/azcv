# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@microsoft.com
#
# A script to create an interesting thumbnail from an image.
#
# ml thumbnail azcv <path>

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

import os
import argparse
from urllib.parse import urlparse
import urllib.error
import urllib.request
import sys

from PIL import Image
import io 			# Create local image.
import re

from mlhub.pkg import is_url
from mlhub.utils import get_cmd_cwd, get_private

# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path or url to image')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# Request subscription key and location from user.
# ----------------------------------------------------------------------

PRIVATE_FILE = "private.json"

path = os.path.join(os.getcwd(), PRIVATE_FILE)

private_dic = get_private(path, "azcv")

if "key" not in private_dic["Computer Vision"]:
    print("There is no key in private.json. Please run ml configure azcv to upload your key.", file=sys.stderr)
    sys.exit(1)

subscription_key = private_dic["Computer Vision"]["key"]

endpoint = private_dic["Computer Vision"]["endpoint"]

# Set credentials.

credentials = CognitiveServicesCredentials(subscription_key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)

# Check the URL supplied or path exists and is an image.

# Send provided image (url or path) to azure to extract text.

url = args.path

width = 50
height = 50

if is_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)

        if urllib.request.urlopen(req).status == 200:
            try:
                analysis = client.generate_thumbnail(width, height, url)
            except Exception as e:
                print(f"Error: {e}\n{url}")
                sys.exit(1)
        sname = re.sub('\.(\w+)$', r'-thumbnail.\1', os.path.basename(urlparse(url).path))
        sname = os.path.join(get_cmd_cwd(), sname)

    except urllib.error.URLError:
        print("Error: The URL does not appear to exist. Please check.")
        print(url)
        sys.exit(1)
else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.generate_thumbnail_in_stream(width, height, fstream)
        except Exception as e:
            print(f"Error: {e}\n{path}")
            sys.exit(1)

    sname = re.sub('\.(\w+)$', r'-thumbnail.\1', path)

for x in analysis:
    image = Image.open(io.BytesIO(x))

image.save(sname)
print(sname)
