import re
import webbrowser
from urllib.request import urlopen
from sys import *


def Find(string):
    url = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', string)
    return url

def WebLauncher(path):
    with open(path) as fp:
        for line in fp:
            url = Find(line)
            for str in url:
                webbrowser.open(str, new=2)

def main():

    WebLauncher(argv[1])

if __name__ == "__main__":
    main()