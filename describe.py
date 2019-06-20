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
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

import os
import argparse
from textwrap import fill

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
    analysis = client.describe_image(path, max_descriptions, language)
else:
    path = os.path.join(get_cmd_cwd(), path)
    with open(path, 'rb') as fstream:
        analysis = client.describe_image_in_stream(fstream, max_descriptions, language)

for caption in analysis.captions:
    print(fill("{} {}".format(round(caption.confidence, 2), caption.text)) + "\n")
