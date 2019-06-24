Azure Computer Vision
=====================

This [MLHub](https://mlhub.ai) package provides a quick introduction
to the pre-built Computer Vision model provided through Azure's
Cognitive Services. This service analyses images to extract
descriptions and text found in the images.

In addition to the demonstration this package provides a collection of
commands that turn the service into a useful command line tool for
ocr, landmark identification, and thumbnail generation.

A free Azure subscription allowing up to 20,000 transactions per month
is available from https://azure.microsoft.com/free/. Once set up visit
https://ms.portal.azure.com and Create a resource under AI and Machine
Learning called Cognitive Services. Once created you can access the web
API subscription key and endpoint from the portal. This will be
prompted for in the demo.

This package is part of the [Azure on
MLHub](https://github.com/Azure/mlhub) repository. Please note that
these Azure models, unlike the MLHub models in general, use *closed
source services* which have no guarantee of ongoing availability and
do not come with the freedom to modify and share.

Visit the github repository for more details:
<https://github.com/Azure/azcv>

The Python code is based on the [Azure Cognitive Services Computer
Vision SDK for
Python](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk)
Quick Start guide.

Usage
-----

- To install mlhub (Ubuntu 18.04 LTS)

```console
$ pip3 install mlhub
```

- To install and configure the demo:

```console
$ ml install   azcv
$ ml configure azcv
```

Command Line Tools
------------------

In addition to the *demo* presented below, the *azcv* package provides
a number of useful command line tools.

*Landmarks and Tags*

The *landmark* command takes an image (url or path to a local file)
and identifies the main landmark contained within the image. The
confidence of the identification is also returned.

```console
$ ml landmark azcv img.jpg
0.95,Marina Bay Sands
```

The *tag* command takes an image (url or path to a local file) and
generates a collection of tags that identify key elements of the
image. Each tag has a confidence.

```console
$ ml tag azcv img.jpg
0.96,landscape
0.86,desert
...
```
See [Landmarks and Tags](TAGS.md) for details.

*Optical Character Recognition*

The *ocr* command is useful for extracting text from a variety of
images. See the specific examples:

```console
$ ml ocr azcv img.jpg
325 305 1297 290 1302 594 329 609,ABBEY
...
```

- [Extract Text for Handwriting](HAND_WRITING.md)
- [Reading Street Signs](STREET.md)
- [Extract Code from Python](CODE.md)

*Thumbnails*

Thumbnails require more than simply generating a small square section
from an image. Ideally it is in some way representative of the
image. The *thumbnail* command will choose a "good" region of the
image to display as a thumbnail.

```console
$ ml thumbnail azcv img.jpg
img-thumbnail.jpg
```

*WorkFlow*

We collect together examples of using the commands within different
workflow pipelines here, including adding bounding boxes by command
line:

- [Workflow Pipelines](WORKFLOWS.md)

Demonstration
-------------

```console
$ ml demo azcv

=========================
Azure Computer Vision API
=========================

Welcome to a demo of pre-built models for Computer Vision. This Azure 
Cognitive Service supports various operations related to Computer Vision.
This MLHub package demonstrates the various services. Other MLHub packages
exist for specific tasks like identifying the landmark in an image
(azlandmark), recoginising words in an image (azocr) and generating
thumbnails from images (azthumb).

An Azure resource is required to access this service (and to run this command).
See the README for details of a free subscription. If you have a subscription
then please paste the key and the endpoint here.

Please paste your Computer Vision subscription key: ********************************
Please paste your endpoint: https://southeastasia.api.cognitive.microsoft.com/

I've saved that information into the file:

    /home/kayon/.mlhub/azcv/private.txt

Press Enter to continue: 

================
Analyze an image
================

We can analyze an image for certain features with analyze_image(). We use the
visual_features= property to set the types of analysis to perform on the image. 
Common values are VisualFeatureTypes.tags and VisualFeatureTypes.description. 

For our demonstration we will analyze the following image:

Location: https://upload.wikimedia.org/
Path:     wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/
Filename: 450px-Broadway_and_Times_Square_by_night.jpg

Press Enter to continue: 

Close the graphic window using Ctrl-w.

Press Enter to continue: 
```
![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/12/Broadway_and_Times_Square_by_night.jpg/450px-Broadway_and_Times_Square_by_night.jpg)

```console
============
Tag Analysis
============

We list the tags for the image together with a measure of confidence.

Confidence: 1.00 Tag: skyscraper
Confidence: 0.99 Tag: building
Confidence: 0.98 Tag: outdoor
Confidence: 0.92 Tag: light
Confidence: 0.91 Tag: street
Confidence: 0.87 Tag: downtown
Confidence: 0.86 Tag: cityscape
Confidence: 0.80 Tag: sky
Confidence: 0.79 Tag: city
Confidence: 0.70 Tag: street light
Confidence: 0.59 Tag: car
Confidence: 0.58 Tag: people
Confidence: 0.42 Tag: busy
Confidence: 0.28 Tag: night

Press Enter to continue: 

===================
Subject Domain List
===================

Various subject domains can be used to analyze images. The domains include
celebrities and landmarks.

celebrities: people_, 人_, pessoas_, gente_

landmarks: outdoor_, 户外_, 屋外_, aoarlivre_, alairelibre_, building_,
    建筑_, 建物_, edifício_

Press Enter to continue: 

==========================
Analyze an Image by Domain
==========================

We can specify a subject domain within which to analyze an image. For example,
below we use the landmarks domain to identify the landmark in an image. See the
separate azlandmark MLHub package for a standalone demonstration and tool.

For our demonstration we will analyze the following image:

Location: https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg
      
Press Enter to continue: 

Close the graphic window using Ctrl-w.

Press Enter to continue: 
```
![](https://images.pexels.com/photos/338515/pexels-photo-338515.jpeg)
```console
Identified "Eiffel Tower" with confidence 0.97.

Press Enter to continue: 

============================
Text Description of an Image
============================

We can obtain a language-based text description of an image and can request
several descriptions for our further text analysis for keywords associated
with the image. 

For our demonstration we will analyze the following image:

Location: http://www.public-domain-photos.com/
Path:     free-stock-photos-4/travel/san-francisco/
Filename: golden-gate-bridge-in-san-francisco.jpg

Press Enter to continue: 

Close the graphic window using Ctrl-w.

Press Enter to continue: 
```
![](http://www.public-domain-photos.com/free-stock-photos-4/travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg)
```console
With confidence of 0.76 found a train crossing Golden Gate Bridge over
a body of water

With confidence of 0.76 found a large bridge over a body of water with
Golden Gate Bridge in the background

With confidence of 0.74 found a train crossing Golden Gate Bridge over
a large body of water

Press Enter to continue: 

===============
Text From Image
===============

We can identify text from an image using Text Recognition Mode. This mode 
supports both handwritten and typed text. The results include the text as well
as the bounding box coordinates for the text so that the image itself can be
marked up with the identified text. See the standalone MLHub package azocr
which can be used as a tool for extracting text from any supplied image.

For our demonstration we will analyze the following image:

Location: https://azurecomcdn.azureedge.net/
Hash:     cvt-1979217d3d0d31c5c87cbd991bccfee2d184b55eeb4081200012bdaf6a65601a/
Filename: images/shared/cognitive-services-demos/read-text/read-1-thumbnail.png

Press Enter to continue: 

Close the graphic window using Ctrl-w.

Press Enter to continue: 
```
![](https://azurecomcdn.azureedge.net/cvt-1979217d3d0d31c5c87cbd991bccfee2d184b55eeb4081200012bdaf6a65601a/images/shared/cognitive-services-demos/read-text/read-1-thumbnail.png)
```console
Found "Sorry!" at [11, 35, 58, 32, 59, 48, 12, 51]

Found "Have a" at [84, 42, 135, 34, 138, 50, 87, 57]

Found "Oops!" at [23, 77, 60, 75, 62, 91, 23, 94]

Found "nice day!" at [82, 56, 148, 50, 150, 68, 84, 73]

Found "See you soon !" at [15, 115, 100, 109, 101, 126, 17, 132]

Found "Bye !" at [123, 96, 153, 95, 154, 112, 123, 113]

Press Enter to continue: 

==================
Generate Thumbnail
==================

A utility provided by the service can generate a thumbnail (JPG) of an image. 
The thumbnail does not need to be in the same proportions as the original
image. Here we create a square 50x50 thumbnail.

For our demonstration we will analyze the following image:

Site: http://www.public-domain-photos.com/free-stock-photos-4/
Path: travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg

Press Enter to continue: 

Close the graphic window using Ctrl-w.

Press Enter to continue: 
```
![](http://www.public-domain-photos.com/free-stock-photos-4/travel/san-francisco/golden-gate-bridge-in-san-francisco.jpg)
```console
Close the graphic window using Ctrl-w.
```
![thumbnail](sample_thumbnail.jpg)
```console
Thank you for exploring the 'azcv' package.
```

# Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.microsoft.com.

When you submit a pull request, a CLA-bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., label, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.

# Legal Notices

Microsoft and any contributors grant you a license to the Microsoft documentation and other content
in this repository under the [Creative Commons Attribution 4.0 International Public License](https://creativecommons.org/licenses/by/4.0/legalcode),
see the [LICENSE](LICENSE) file, and grant you a license to any code in the repository under the [MIT License](https://opensource.org/licenses/MIT), see the
[LICENSE-CODE](LICENSE-CODE) file.

Microsoft, Windows, Microsoft Azure and/or other Microsoft products and services referenced in the documentation
may be either trademarks or registered trademarks of Microsoft in the United States and/or other countries.
The licenses for this project do not grant you rights to use any Microsoft names, logos, or trademarks.
Microsoft's general trademark guidelines can be found at http://go.microsoft.com/fwlink/?LinkID=254653.

Privacy information can be found at https://privacy.microsoft.com/en-us/

Microsoft and any contributors reserve all other rights, whether under their respective copyrights, patents,
or trademarks, whether by implication, estoppel or otherwise.
