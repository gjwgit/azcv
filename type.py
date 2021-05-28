# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@togaware.com
#
# A script to identify celebrities in a photo.
#
# ml celebrities azcv <path>
#

from azure.cognitiveservices.vision.computervision import ComputerVisionClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.computervision.models import VisualFeatureTypes

import os
import sys
import argparse

from mlhub.pkg import is_url, get_cmd_cwd, get_private

import urllib.error
import urllib.request
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

# Send image to azure to analyse.

url = args.path

features = [VisualFeatureTypes.image_type]

if is_url(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=headers)
        if urllib.request.urlopen(req).status == 200:
            try:
                analysis = client.analyze_image(url, features)
            except Exception as e:
                catch_exception(e, url)

    except urllib.error.URLError:
        sys.exit("Error: The URL does not appear to exist. Please check.\n"
                 f"{url}")

else:
    path = os.path.join(get_cmd_cwd(), url)
    with open(path, 'rb') as fstream:
        try:
            analysis = client.analyze_image_in_stream(fstream, features)
        except Exception as e:
            catch_exception(e, path)

if analysis:
    ca = analysis.image_type.clip_art_type
    ld = analysis.image_type.line_drawing_type

    cat = ""
    if ca == 0:
        cat = "no"
    elif ca == 1:
        cat = "ambiguous"
    elif ca == 2:
        cat = "ok"
    elif ca == 3:
        cat = "good"

    ldt = ""
    if ld == 0:
        ldt = "no"
    elif ld == 1:
        ldt = "yes"

    print(f"{cat},{ldt}")
