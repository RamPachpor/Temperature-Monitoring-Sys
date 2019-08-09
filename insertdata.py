import urllib.request
from bs4 import BeautifulSoup
import random
import time
while 1:
    a=random.randint(1,101)
    data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=O5ILSWY749XR3KL3&field1="+str(a))
    time.sleep(10)