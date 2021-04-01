{"type":"level", "id":"2","description":"My job is to keep 50 power motors running ok. I need AI to cover this task. "}

## 과제목표
50톤이하 무인운전 소규모 정화설비의 핵심인 배수펌프의 모터 작동 이상여부를 실시간 탐지하는 인공지능 소프트웨어 개발

## 배경
IoT 전문회사인 MeasureWare 스타트업에 취업해서 맡은 임무가 학교, 대형식당 등 소규모 무인정화 전동펌프의 정상가동을 책임지는 것이며, 실시간으로 모터의 이상작동을 탐지하는 소프웨어를 만든다. 메저웨어사는 가스미터, 전기미터등 각종 레거시 계량기들의 실시간 데이터 특정을 기반으로 하는 사업전략을 수립중

## 보유하고 있어야 할 badge
* I can do "Prediction of Time Series Data"

    https://tykimos.github.io/2017/09/09/Time-series_Numerical_Input_Numerical_Prediction_Model_Recipe/ 
## 다음단계 Level 추천
## 획득 Badge
## List of Missions
* Mission1: 모터의 전력사용 데이타를 데이타베이스로 부터 읽어온다.
* Mission2: 탐지할 목적에 따라 data featuring 을 위한 프로그램 구성, 데이타 특성을 살펴보고 최적의 look back 파라미터를 소정의 시행착오를 거쳐 찾는 과정 필요
* Mission3: LSTM 알고리듬 적용을 위한 Training/Testing 데이타셋 구성
* Mission4: Training 진행 Model 저장
* Mission5: Model를 사용하여 예측기능 구현 및 예측값과 실제값을 비교하는 기능 구현
* Mission6: Anomaly를 수학적으로 정의하고 프로그램 구현
* Mission7: Anomaly 탐지시 delivery 기능 구현
* Remarks: Human-Friendly형태로 구성한 이 형태는 간단한 Preprocessing을 통해 Computer-Friendly JSON으로 변환한다. 한줄은 ':'으로 구분되어 ':' 앞부분은 black제거후 Key로, ':' 뒷부분은 Value로 변환한다
