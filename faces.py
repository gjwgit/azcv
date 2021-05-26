# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to detect faces in an image.
#
# ml faces azcv <path>

from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision import ComputerVisionClient

import os
import argparse
import requests
import sys

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
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

subscription_key, endpoint = get_private()

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

image_features = ["faces"]

# Send provided image (url or path) to azure to analyse.

if is_url(path):
    request = requests.get(path)
    if request.status_code != 200:
        sys.exit(f"Error: The URL does not appear to exist. Please check.\n{path}")
    try:
        analysis = client.analyze_image(path, image_features)
    except Exception as e:
            if "PermissionDenied" in str(e) or "Endpoint" in str(e):
                sys.exit(f"{e}\n"
                         f"Please run 'ml configure azcv' to update your private information. ")
            else:
                sys.exit(f"Error: {e}\n{path}")
else:
    path = os.path.join(get_cmd_cwd(), path)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.analyze_image_in_stream(fstream, image_features)
        except Exception as e:
            if "PermissionDenied" in str(e) or "Endpoint" in str(e):
                sys.exit(f"{e}\n"
                         f"Please run 'ml configure azcv' to update your private information. ")
            else:
                sys.exit(f"Error: {e}\n{path}")

for face in analysis.faces:
        print(f"{face.face_rectangle.left} {face.face_rectangle.top} " +
              f"{face.face_rectangle.left + face.face_rectangle.width} " +
              f"{face.face_rectangle.top + face.face_rectangle.height}," +
              f"{face.gender},{face.age}")
