## Digital Twin Meter
  머신러닝으로 인식한 숫자를 웹상에서 다시 digital image로 표출하여 digital twin meter를 구성한다.
  
  마지막으로  저장된 값을 미터(디지탈트윈)에 표시
  http://54.180.106.144:8080/meter  
  
  새 값을 저장하고 미터(디지탈트윈)에 표시
  http://54.180.106.144:8080/meter/1234.5

## Actuation
눈으로는 디지탈로 표현된 미터 이미지를 볼 수 있고, 인식된 숫자로는 필요한 액션을 할 수 있다.
slack의 web hookup 으로 meter값의 증가이벤트시 메시지를 푸시 한다.

## 미리 만들어진 모델의 로딩

미리 모델이 다음 위치에 만들어져 있음을 전제로 한다.

  ./05_apply_MNIST/model 

./model 의 내용이 비이었거나 veryfy_model.ipynb 의 실행에 오류가 있다면, 위의 폴더위치에서
아래의  링크를 통해 model을 다운로드 받고 설치해 둔다.

https://drive.google.com/file/d/1sa3dAdiMQzppiJV7o6Co9_fVoq1nucGW/view?usp=sharing