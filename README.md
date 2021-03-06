# bme547-final-project
Image Processor Final Project (Spring 2019)

[![Build Status](https://travis-ci.org/mhuss93/bme547final.svg?branch=master)](https://travis-ci.org/mhuss93/bme547final)

[![Documentation Status](https://readthedocs.org/projects/bme547final/badge/?version=latest)](https://bme547final.readthedocs.io/en/latest/?badge=latest)

## Overview of Project and GUI functionality:
In this project we develop an image processing server. A client operates the server using a GUI
that allows to choose a picture or several picture of type .JPG, .PNG, or .TIFF from their hard drive.
This picture is then encoded into a string and can then be uploaded to the server, where it is stored in a database as an encoded string of the RGB array. The database additionally stores the user ID, the time of upload and the duraiton of processing of the image.
The client has 4 option for processing the image: Histrogram Equalization (default), Contrast Stretching, Log Compression and Reverse Video. The processed image is stored on the server in the same encoded rgb array format, and is also sent back to the user. The user can compare the original and processed image visually in the GUI, as well as plot the color histograms of both images. The dropdown menu can also be used to access and process previous images that have been stored to the database.

## Setting up the program:
Run the bme547final_gui.py file to activate the GUI.

## Guide for using GUI:
1. You MUST enter a user ID and click the 'Enter ID' button
2. Browse - click browse to choose an image of folder of images to be processed
3. On left side of window, click a radio button of the process you want to have performed on your image.
4. Alternatively one can just click on Process Image and then choose an already stored image to be processed. This only works for images that have been previously uploaded to the database.
5. Process Image - press this button to process the image(s)
6. A second window now pops up. It displays the original and processed image.
7. Display Histograms - pressing this button will display the histrograms for both images.
