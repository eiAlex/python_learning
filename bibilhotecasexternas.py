from urllib.request import urlopen
html = urlopen("http://www.google.com/")
#print(html.read())

import urllib 
url = 'http://github.com/eiAlex/Python-Lerarning/blob/master/TesteBibilhotecasExterna.py'
arqu = urlopen(url)
#print(arqu.read())
open('TesteBibilhotecasExterna.py').write(arqu.read())