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

fswebcam은 USB 카메라에 대한 구동명령어이다. Bus로 연결되는 RPi Camera의 경우는 faspistill 명령을 사용한다.

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

## MagicEco Reference WebSensor Info
* Real time meter reading image:  http://bit.ly/websensor1 
