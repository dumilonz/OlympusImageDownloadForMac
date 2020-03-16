from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import html5lib
from datetime import datetime

URL = "http://192.168.0.10/DCIM/100OLYMP/"
array_start = "wlansd = new Array();"
array_end = "wlansd.sort(cmptime);"
already_downloaded = open('./downloads/downloadList.txt', 'r+').read()
update_downloads = open('./downloads/updatedDownloads.txt', 'a+')

def main():
    try:
        soup = BeautifulSoup(urlopen(URL), 'html5lib')
        display_script = str(soup.find_all('script'))
        print('Connected to ', URL)

        download_array = get_download_array(display_script)
        print('Retrieved ' + str(len(download_array)) + ' pictures to download...')

        download_pictures(download_array)
        update_downloads.close()
        print('Done...')
    except ConnectionRefusedError:
        print('ERROR: Make sure you\'re connmected to the Olympus WiFi and rerun ')
        return 0

    return 1

def get_download_array(display_script):
    photo_array = display_script[display_script.index(array_start)+len(array_start):redirect_script.index(array_end)]
    array_size = int(photo_array[photo_array.rindex('[') + 1 :photo_array.rindex(']')]) + 1
    wlansd = [None] * array_size
    exec(photo_array)
    
    new_downloads = []
    for el in wlansd:
        filename = el[el.index(',') + 1: el.find(',', el.find(',') + 1)]
        if '.ORF' not in filename and filename not in already_downloaded:
            new_downloads.append(filename)
    return new_downloads

def download_pictures(image_array):
    i = 1
    num_downloads = len(image_array)
    print('Starting download...')
    for image_name in image_array:
        try:
            print(str(i) + 'of ' + str(num_downloads) + ': ' + image_name)
            f = open("./downloads/" + image_name, 'wb')
            f.write(urlopen(URL + image_name).read())
            f.close()
            i = i + 1
            update_downloads.write(str(datetime.now()) + ' - ' + image_name + '\n')
            
        except ConnectionRefusedError:
            print('ERROR: Make sure you\'re connmected to the Olympus WiFi. Run 2nd script and rerun ')
        except: 
            print('ERROR: could not download', image_name, '\n')

if __name__ == '__main__':
    exit(main())