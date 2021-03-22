## 실시간 미터 이미지 취득
* Raspberry Pi의 USB카메라를 통해 이미지를 캡처한다. crontab 스케줄링을 통해 이미지를 캡처한다.
* 캡처된 이미지를 cloud server로 보낸다.  클라우드서버에는 Flask로 작은 웹서버를 만들어 last image를 받아오는 API를 구현하여 카메라 디바이스와 independent한 구조를 만든다.
* 미터값 인식 머신러닝 프로그램은 실시간 인식을 위해 HTTP API 콜을 통해 이미지를 취득한다.

## MagicEco WebSensor Info
* Real time meter reading image
* http://54.180.106.144:8080/websensor 
