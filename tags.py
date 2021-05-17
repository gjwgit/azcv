# -*- coding: utf-8 -*-

# Original code Copyright (c) Microsoft Corporation. All rights reserved.
# New code Copyright (c) Graham.Williams@Togaware. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com.com
#
# A command line script to propose tags for an image.
#
# ml tag azcv <path>

# ----------------------------------------------------------------------
# Setup
# ----------------------------------------------------------------------

# Import the required libraries.

import os
import argparse
import requests
import sys

from mlhub.pkg import is_url, get_cmd_cwd, get_private

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes


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

# Check the URL supplied or path exists and is an image.

# Send provided image (url or path) to azure to extract text.

url = args.path

if is_url(url):
    request = requests.get(url)
    if request.status_code != 200:
        print(f"Error: The URL does not appear to exist. Please check.\n{url}")
        quit()
    try:
        analysis = client.analyze_image(url, visual_features=[VisualFeatureTypes.tags])
    except Exception as e:
        print(f"Error: {e}\n{url}")
        quit()
    
else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        # https://docs.microsoft.com/en-us/azure/cognitive-services/custom-vision-service/limits-and-quotas
        size=os.path.getsize(path)/1000000
        if size > 4:
            print(f"The image file is too large for Azure at {size:.2} MB > 4.0 MB. Reduce and try again.")
            print(f"    {path}")
            print("\nFor example, use imagemagick's convert command:")
            print(f"    $ convert {path} -resize 25% new.jpg\n")
            exit()
        try:
            analysis = client.analyze_image_in_stream(fstream, visual_features=[VisualFeatureTypes.tags])
        except Exception as e:
            print(f"Error: {e}\n{path}")
            quit()
   
for tag in analysis.tags:
    if tag.confidence > 0.2:
        print("{:4.2f},{}".format(round(tag.confidence, 2), tag.name))
