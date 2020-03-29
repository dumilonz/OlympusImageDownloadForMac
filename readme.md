# Mac Olympus Wifi connected image downloader

## Introduction
This is a dockerized python application that downloads new pictures from your Olympus camera to your local filesystem. 

## Installation

## How it works
1. Ensure that you computer is connected to your Olympus WiFi hotspot.
2. Open up a Terminal.
3. Run the following commands:
```bash
    docker build -t olympus_downloader .
    docker run -it olympus_downloader sh 
```
4. In the next line run:
```bash
    python odown.py 
```

When the program is done running (You must see the code output **Done...** in the terminal):

5. Open a new, second terminal (without closing the first terminal or terminating the docker container)
6. Run the following bash file 
```bash
    ./move_files
```

When this bash script has finished you can terminate all docker containers and close all terminals. Your photos will be downloaded into the downloads folder.

