# Mac Olympus Wifi connected image downloader

## Introduction
This is a dockerized python application that downloads new photos and videos taken on your Olympus camera to your local file system. 

## Installation
1. Ensure that you have Docker installed on your local machine.
2. From Gitlab download this project.

## Process
1. Ensure that you computer is connected to your Olympus WiFi hotspot. Stay connected to this hotspot until you have completed the downloading process (step 6).
2. Open up a terminal.
3. Run the following commands in the command line:
```bash
    DOCKER_ID='olympus_downloader'
    docker build -t $DOCKER_ID .
    docker run -it $DOCKER_ID sh 
```
4. In the command line of the docker container (the current available line) run:
```bash
    python odown.py 
```

When the python program has completed downloading the photos to the docker container (You must see the code output **Done...** in the terminal):

5. Open a new, second terminal (**Do not close the first terminal or the docker container**)
6. Run the following bash file in the second terminal
```bash
    ./move_files
```

When this bash script has completed you can terminate all docker containers and close all terminals. Your photos will be downloaded into the *./OlympusDownloader/downloads* folder on your local machine.
