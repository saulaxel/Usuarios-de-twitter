
from HTMLParser import HTMLParser
import re
from re import sub
from sys import stderr
import urllib
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

## Clase para parsear una pagina (Twitter)  ##
## Fuente: http://stackoverflow.com/questions/328356/extracting-text-from-html-file-using-python ##

class _DeHTMLParser( HTMLParser ):
    def __init__(self):
        HTMLParser.__init__(self)
        self.__text = []

    def handle_data(self, data):
        text = data.strip()
        if len(text) > 0:
            text = sub('[ \t\r\n]+', ' ', text)
            self.__text.append(text + ' ')

    def handle_starttag(self, tag, attrs):
        if tag == 'p':
            self.__text.append(' ')

    def text(self):
        return ''.join(self.__text).strip()


def dehtml(text):
    try:
        parser = _DeHTMLParser()
        parser.feed(text)
        parser.close()
        return parser.text()
    except:
        return text


Twitter = urllib.urlopen("https://twitter.com/?lang=es")

algo = Twitter.read()

algo = dehtml( algo )

parrafo = re.findall('............................................................................................................................................?',algo)

archivo = open("Texto.txt", "w")

for i in range ( 0, len(parrafo) ):
	archivo.write(parrafo[i])
	archivo.write("\n\n")


archivo.close()