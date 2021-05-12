{"type":"level"}
https://innovationacademy.kr/project#projectx 
# Men working!

## 산출물
### 1. 전문트랙용 Level (8주짜리) - 우리가 흔히 말하는 프로젝트형태
#### 목적: 기업체 프로젝트 진행과정 
##### 2가지 목적
   - 기업체의 필요로 하는 인재의 qualification 확인용
   - 기업체가 풀어야 하는 문제에 도전해서 의미있는 성과를 내는 인재 filtering용
   위 2가지 모드 샘플 솔루션 케이스가 주어져야함
  
   기업체가 프로젝트를 구성하는데 필요한 Template및 예제  
       https://innovationacademy.kr/notice?board=4&label=10&post=104 
   필요한 내용
   - Level이 풀고자하는 사업적, 가치적 목표제시
   - 미션 단위 구성과 각 미션당 풀어야할 기술적 산출물 제시
   - 이 Level을 풀기위해 필요한 역량(Badge)들 제시
   
### 2. 공통트랙용 Level (2주짜리)
### 목적: 역량(Badge)획득과정 
   기업체 프로젝트 (Level)에 기술된 필요역량 단위(Badge)를 획득하는 과정 
   Badge예시)
````
       image badge: 이미지화일에 대한 opencv API call에 가능
       tesseract badge: google tesseract api call에 가능
       image categorization data labelling badge: 수만장의 label된 이미지를 training image library로 구성 가능
       image categorization machine learning badge: Fashion MNIST 형태의 머신러닝 알고리듬을 실행 가능
       time series data의 prediction badge: 시계열 데이타의 예측을 위한 LSTM 알고리듬을 위한 데이타 구성 가능
       time series data의 anomaly detection badge: LSTM의 prediction을 응용한 anomaly 탐지
       
       django badge: django framework 사용가능
       django/apache badge: django apache2 구성가능
````       

### 3. 디렉토리 화일 구성
#### 오픈소스로 구성된 Project-X의 Level library 는 두가지로 구성
    - 학생에게 주는 challenge파트
        README.MD 화일로 저장
    - 멘토들이 참고할 내용 (비공개를 전제)
        CHEAT_SHEET.MD 화일로 저장

#### 레벨화일 전체 스캔
    - scan.py 는 디렉토리 하부의 Level 정의 화일을 scan하여 자동으로 README.MD를 파싱하여 전체 Level에 대한 정의를 Google Spreadsheet에 저장
    - Level의 메타정보를 별도로 관리하는 것이 아니라, 해당 Repository내 README.MD 내에 관리하여 데이타의 일관성유지의 편의를 도모한다.

#### Online Playbook JSON정의 (Google Spreadsheet기반으로 이것이 master version)
    - http://
### 4. 레벨, 미션수행, 평가 절차 및 평가양식

http://bit.ly/IA_playbook
