## Digital Twin Meter
  머신러닝으로 인식한 숫자를 웹상에서 다시 digital image로 표출하여 digital twin meter를 구성한다.
  
  마지막으로  저장된 값을 미터(디지탈트윈)에 표시
  http://54.180.106.144:8080/meter  
  
  새 값을 저장하고 미터(디지탈트윈)에 표시
  http://54.180.106.144:8080/meter/1234.5

## Actuation
눈으로는 디지탈로 표현된 미터 이미지를 볼 수 있고, 인식된 숫자로는 필요한 액션을 할 수 있다.
slack의 web hookup 으로 meter값의 증가이벤트시 메시지를 푸시 한다.
