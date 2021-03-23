Azure Computer Vision
=====================

This documentation is also published at 
[Read The Docs](https://mlhub-azcv.readthedocs.io/en/latest/).

This [MLHub](https://mlhub.ai) package provides a demonstration, a
graphical user interface, and command line tools that utilise
pre-built models from [Azure Computer
Vision](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision). Individual
command line tools are packaged for common computer vision tasks
including image analysis to extract descriptions of the images, word
recognition from images, landmark identification, thumbnail
generation, and more. The command line tools can be used within
command pipelines for tasks including the tagging of personal photos
folder, analysis of images from a cameras monitoring a bird feeder,
reading street signs to support a driver, and reading handwritten
texts.

A free Azure subscription allowing up to 5,000 transactions per month
with a maximum of 20 per minute (according to [Azure
Pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/computer-vision/))
is available from <https://azure.microsoft.com/free/>. After
subscribing visit <https://portal.azure.com> and Create a resource
under AI and Machine Learning called Cognitive Services. Once created
you can access the web API subscription key and endpoint from the
portal. This will be prompted for when running a command, and then
saved to file to reduce the need for repeated authentication requests.

Please note that these Azure models, unlike the MLHub models in
general, use *closed source services* which have no guarantee of
ongoing availability and do not come with the freedom to modify and
share.

Visit the github repository for more details:
<https://github.com/gjwgit/azcv>

The Python code is based on the [Computer Vision client library for
Python Quickstart](https://docs.microsoft.com/en-us/azure/cognitive-services/Computer-vision/quickstarts-sdk/python-sdk)
Quick Start guide.

Quick Start Command Line Examples
---------------------------------

```console
ml category azcv https://bit.ly/3lfNVG6
ml landmarks azcv https://bit.ly/3vnuG24
ml tags azcv https://bit.ly/3cqDonC
ml celebrities azcv https://bit.ly/2OoC9xr
ml objects azcv  https://bit.ly/3eFlaSe
ml ocr azcv https://bit.ly/2Op1qYk
ml ocr azcv https://bit.ly/38F0FBj
ml thumbnail azcv https://bit.ly/3cqDonC
ml brands azcv https://bit.ly/3qIKBo1
ml faces azcv https://bit.ly/38GgwPP
ml color azcv https://bit.ly/3qHlAcY
ml type azcv https://bit.ly/3bNGSBv
```

See <https://mlhub.ai/survivor/azcv.html> for details of the package.

Usage
-----

- To install and configure mlhub (Ubuntu LTS)

```console
$ pip3 install mlhub
$ ml configure
```

- To install and configure the package:

```console
$ ml install   azcv
$ ml configure azcv
$ ml readme    azcv
$ ml commands  azcv
```

- To run a canned demonstration or an interactive GUI:

```console
$ ml demo azcv
$ ml gui azcv
```
