import urllib.request
from bs4 import BeautifulSoup
import random
import time

while(True):
    val=random.randint(1,100)
    data=urllib.request.urlopen("https://api.thingspeak.com/update?api_key=O5ILSWY749XR3KL3&field1="+str(val))
    print(data)
    time.sleep(5)


