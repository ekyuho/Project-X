## Digital Twin Meter
  실시간(1시간 간격등 등간격)으로 capture한 meter 이미지를 머신러닝으로 문자인식하여 웹상에서 다시 digital image로 표출하여 digital twin meter를 구성한다.

## Actuation
눈으로는 디지탈로 표현된 미터 이미지를 볼 수 있고, 인식된 숫자로는 필요한 액션을 할 수 있다.
slack의 web hookup 으로 meter값의 증가이벤트시 메시지를 푸시 한다.
