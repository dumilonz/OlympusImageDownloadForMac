# Mac Olympus Wifi connected image downloader

## Introduction
This is a dockerized python application that dopwnloads new pictures from your Olympus camera to your local filesystem. 

## Installation

## How it works
1. Ensure that you computer is connected to your Olympus WiFi hotspot.
2. Open up a Terminal.
3. Run the following commands:
''' 
    docker build -t olympus_downloader .
    docker run -it olympus_downloader sh 
'''
4. In the next line run:
''' python odown.py '''
When the program is done running (You must see the lines **Done..**):
5. Open a new terminal (without closing the first terminal)
6. Run the following 3 commands:
'''
    docker cp olympus_downloader:/usr/app/downloads/. ./downloads
    rm downloads/downloadList.txt 
    mv downloads/updatedDownloads.txt downloads/downloadList.txt
'''


