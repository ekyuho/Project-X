{"type":"mission","id":"0","description":"실시간 미터 이미지 취득 시스템 구축","mood":"best"}
## 실시간 미터 이미지 취득 시스템 구축
* 라즈베리파이를 수도계량기 바로옆에 설치하고 카메라를 부착하여 Edge Computing 과 같은 구성으로 시스템을 구성하는 방법, 또는 카메라로 취득된 이미지를 클라우드 서버로 보내거나, 클라우드 서버에서 카메라 이미지를 원격에서 취득하게 할 수 있는 방법 등 중에서 고려한다.
* 빛이 없는 지하실에 설치된 수도메터를 읽어야 하는 상황들이 있다.

### take_picture.sh 
Raspberry Pi shell 화면에서 crontab -e 명령을 통해 다음과 같이 설정하여 1시간 단위로 자동으로 실행되도록 설정한다.  다른 빈도의 주기가 필요하면 crontab 명령어 설명을 참조하여 내용을 수정하도록 한다.

```
# m h  dom mon dow   command
0 * * * * /home/pi/Pictures/take_picture.sh >> /home/pi/Pictures/take.sh.log
```

fswebcam은 USB 카메라에 대한 구동명령어이다. Bus로 연결되는 RPi Camera의 경우는 raspistill 명령을 사용한다.

``` 
# take_picture.sh 의 내용
# fswebcam is for USB camera
# raspistill is for RPi bus camera
#
# crontab periodically run this script
#!/bin/bash
DATE=$(date +"%Y-%m-%d_%H%M")
fswebcam -r 1280x720 --font luxisr:24 --title $DATE /home/pi/Pictures/$DATE.jpg
#raspistill -o /home/pi/Pictures/$DATE.jpg

# Once take a picture, it upload to implement http://bit.ly/websensor1
/usr/bin/python3 upload.py $DATE.jpg
```

### upload.py
jpg 이미지를 웹서버로 보내어서 웹주소를 통해 이미지를 가져갈 수 있도록 해주는 징검다리 서버, 일종의 이미지 캐시서버이다. 

```
# upload.py
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
```

### web.js - upload.py에 대응하는 Web server
다음은 upload.py 의 post 를 받는 node.js/express framework 웹서버 코드의 해당 부분
```
var express = require('express');
var app = express()

var buffer_old = ""

app.get('/websensor', function(req,res) {
    if (buffer_old == "") res.end("Meter image will be provided within an hour. Please try again later")
    else res.end(buffer_old)
})

app.post('/websensor', function (req, res) {
    if (req.body == undefined) {
        buffer = new Buffer.alloc(0)
        req.on('data', function(chunk) {
            buffer = Buffer.concat([buffer, chunk])
        });

        req.once('end', function() {
            console.log(`done ${buffer.length}B`)
            buffer_old = buffer
            res.end("{X-ACK}")
        });
    } else res.end("{X-NACK}")
})

var server = app.listen(8080, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("listening at http://%s:%s", host, port)
})
```
## 실시간 작동중인 Web Sensor URL
* Real time meter reading image:  http://bit.ly/websensor1 
