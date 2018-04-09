import requests
#import json
URL = "http://192.168.1.3:5000/"

files = {'image':open('/home/pi/Desktop/groups/picg8.jpg')}

r=requests.post(URL, files=files)
#r.json()
print(r.text)
