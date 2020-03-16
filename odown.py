from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup
import html5lib
def main():
    try:
        soup = BeautifulSoup(urlopen(URL), 'html5lib')
        redirect_script = str(soup.find_all('script'))
        print('Connected to ', URL)

    except ConnectionRefusedError:
        print('ERROR: Make sure you\'re connmected to the Olympus WiFi and rerun ')
        return 0

    return 1

if __name__ == '__main__':
    exit(main())