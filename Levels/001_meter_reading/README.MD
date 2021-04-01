{"type":"level","id":"1","description":"Company would hire me if I'm able to build software system to reconize water meter."}

## 과제목표
수도 계량기 계측기 미터값 읽기
## 배경
IoT 전문회사인 MeasureWare 스타트업에 취업해서 맡은 임무가 가정용 수도계량기의 미터값을 읽어들이는 것이다. 메저웨어사는 가스미터, 전기미터등 각종 레거시 계량기들의 실시간 데이터 특정을 기반으로 하는 사업전략을 수립중

## 보유하고 있어야 할 badge

* I can do "Fashion MNIST"

    https://www.tensorflow.org/tutorials/keras/classification 

## 다음단계 Level 추천

## 획득 Badge

## List of Missions
* Mission1: 숫자가 표시되는 계량기의 숫자표시부의 image를 읽어들여서 읽어들이고자 하는 숫자부분의 이미지를 추출한다. 다음의 과정들을 사용한다.
    1. 회전  2. 광각뷰 보정  3. crop  4. gray scale로 변환, 숫자부문 추출한 이미지 출력.
* Mission2: Mission1의 이미지를 낱자 단위로 분리하고, 구글 API를 이용하여 문자인식하여 출력한다.
* Mission3: 주어진 수도계량이 이미지화일을 다운로드 받아 Tensorflow의 Fashion MNIST 알고리듬을 적용을 위한 Labelled 데이타셋을 만든다.
* Mission4: Mission 3에서 만든 데이타셋으로 Fashion MNIST 알고리듬을 이용 training을 시키고 숫자인식 시스템을 완성한다.
* Remarks: Human-Friendly형태로 구성한 이 형태는 간단한 Preprocessing을 통해 Computer-Friendly JSON으로 변환한다.  한줄은 ':'으로 구분되어 ':' 앞부분은 black제거후 Key로, ':' 뒷부분은 Value로 변환한다
