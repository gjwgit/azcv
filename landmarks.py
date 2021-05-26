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
# Request subscription key and endpoint from user.
# ----------------------------------------------------------------------

subscription_key, endpoint = get_private()

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
                if "PermissionDenied" in str(e) or "Endpoint" in str(e):
                    sys.exit(f"{e}\n"
                             f"Please run 'ml configure azcv' to update your private information. ")
                else:
                    sys.exit(f"Error: {e}\n{url}")

    except urllib.error.URLError:
        sys.exit("Error: The URL does not appear to exist. Please check.\n"
                 f"{url}")

else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.analyze_image_by_domain_in_stream(domain, fstream, language)
        except Exception as e:
            if "PermissionDenied" in str(e) or "Endpoint" in str(e):
                sys.exit(f"{e}\n"
                         f"Please run 'ml configure azcv' to update your private information. ")
            else:
                sys.exit(f"Error: {e}\n{url}")
    
for landmark in analysis.result["landmarks"]:
    print('{},{}'.format(round(landmark["confidence"],2), landmark["name"], ))

# Write results to stdout

# Generate locally annotated image

