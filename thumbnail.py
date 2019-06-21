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
from textwrap import fill
from PIL import Image
import io 			# Create local image.
import re

from mlhub.pkg import azkey, is_url
from mlhub.utils import get_cmd_cwd

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

subscription_key, endpoint = azkey(KEY_FILE, SERVICE, verbose=False)

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
    analysis = client.generate_thumbnail(width, height, url)
    sname = re.sub('\.(\w+)$', r'-thumbnail.\1', os.path.basename(urlparse(url).path))
else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        analysis = client.generate_thumbnail_in_stream(width, height, fstream)
    sname = re.sub('\.(\w+)$', r'-thumbnail.\1', os.path.basename(url))

for x in analysis:
    image = Image.open(io.BytesIO(x))

image.save(sname)
print(sname)
