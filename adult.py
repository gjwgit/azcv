# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to detect adult content in an image.
#
# ml adult azcv <path>

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

import os
import argparse
import sys

import urllib.error
import urllib.request

from mlhub.pkg import is_url, get_cmd_cwd, get_private

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

subscription_key = private_dic["Computer Vision"]["key"]

endpoint = private_dic["Computer Vision"]["endpoint"]

# Set credentials.

credentials = CognitiveServicesCredentials(subscription_key)

# Create client.

client = ComputerVisionClient(endpoint, credentials)

# ----------------------------------------------------------------------
# URL or path
# ----------------------------------------------------------------------

path = args.path

# Check the URL supplied or path exists and is an image.

# ----------------------------------------------------------------------
# Analyze
# ----------------------------------------------------------------------

image_features = ["adult"]

# Send provided image (url or path) to azure to analyse.

if is_url(path):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(path, headers=headers)
        if urllib.request.urlopen(req).status == 200:
            try:
                analysis = client.analyze_image(path, image_features)

            except Exception as e:
                print(f"Error: {e}\n{path}")
                sys.exit(1)

    except urllib.error.URLError:
        print("Error: The URL does not appear to exist. Please check.")
        print(path)
        sys.exit(1)

else:
    path = os.path.join(get_cmd_cwd(), path)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.analyze_image_in_stream(fstream, image_features)
        except Exception as e:
            print(f"Error: {e}\n{path}")
            sys.exit(1)


print(f"{analysis.adult.adult_score:.2f}," +
      f"{analysis.adult.racy_score:.2f}," +
      f"{analysis.adult.gore_score:.2f}")
