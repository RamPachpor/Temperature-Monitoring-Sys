import urllib.request
import json



TS = urllib.request.urlopen("https://api.thingspeak.com/channels/572348/feeds.json?results=1")

response = TS.read()
data=json.loads(response)


a=data['channel']['id']
feild_1=data['feeds']
    
t=[]
for x in feild_1:
    #print(x['field1'])
    t.append(x['field1'])



