FROM python:3

WORKDIR /usr/app/

COPY requirements.txt .

RUN pip install -r requirements.txt
RUN mkdir -p downloads

COPY odown.py .
COPY ./downloads/downloadList.txt ./downloads/
RUN cp ./downloads/downloadList.txt ./downloads/updatedDownloads.txt

CMD [ "python", "./odown.py" ]