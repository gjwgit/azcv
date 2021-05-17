# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to identify a landmark in a photo.
#
# ml landmark azcv <path>
#

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials

import os
import sys
import argparse
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

# Check the URL supplied. Also want to support local file.

# Send image to azure to identify landmark

# url = "https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg"

url = args.path

domain = "landmarks"
language = "en"

if is_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)

        if urllib.request.urlopen(req).status == 200:
            try:
                analysis = client.analyze_image_by_domain(domain, url, language)
            except Exception as e:
                print(f"Error: {e}\n{url}")
                sys.exit(1)

    except urllib.error.URLError:
        print("Error: The URL does not appear to exist. Please check.")
        print(url)
        sys.exit(1)

else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.analyze_image_by_domain_in_stream(domain, fstream, language)
        except Exception as e:
            print(f"Error: {e}\n{path}")
            sys.exit(1)
    
for landmark in analysis.result["landmarks"]:
    print('{},{}'.format(round(landmark["confidence"],2), landmark["name"], ))

# Write results to stdout

# Generate locally annotated image

