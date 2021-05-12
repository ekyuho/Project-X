import requests
import sys

if len(sys.argv)<2:
    print('no file')
    sys.exit()

url='http://54.180.106.144:8080/websensor'
file=sys.argv[1]
with open(file, 'rb')as f: image=f.read()
r = requests.post(url, data=image, headers={'Content-Type': 'application/octet-stream'})
print(file, r.text)
