{"type":"mission","id":"5","description":"make labelling and build training dataset from files"}

## Fashion MNIST 알고리듬을 활용하는 계량기 숫자인식 시스템 데이타 구축

### 다음의 화일을 다운로드 받는다.

  ./meter_image 
  
3082개의 계량기 이미지가 저장되어야할 위치이다. 화일크기때문에 github가 아닌 구글드라이브 링크를 통해 다운로드받아서 위의 디렉토리에 풀어넣는다.

https://drive.google.com/file/d/1Cgy-iSeiiA4I5v9MHWwsY8MnxoBaKs1A/view?usp=sharing

  ./digits_image

위의 계량기 이미지를 처리하여 낱글자를 저장해두는 위치이다. meter_image로부터 생성되는 2차적인 화일위치이다. 가공 결과물을 먼저 확보하고 싶을 경우 다운로드 받는다.

https://drive.google.com/file/d/1GNeAKevC5upyup9Df2XrGKQmCErHjrbX/view?usp=sharing 

### generate_digit_files.ipynb

계량기 이미지로부터 낱글자를 추출하고, google tesseract API를 이용하여 문자인식을 한다.
tesseract에서 문자인식된 결과를 주었을 경우는, 인식된 숫자를 화일명 앞에 붙여 후에 레이블 정보로 활용할 수 있도록 한다.
tesseract에서 인식이 실패하여 blank가 리턴되었을 경우는 'X'를 화일명 앞에 붙인다. 낱글자 화일은  ./digits_image 폴더에 생성된다.

숫자 낱글자 화일 생성 및 화일명에 레이블링 정보를 붙인후, 수작업으로 레이블링이 잘못된 부분들을 수정하는 작업이 진행되어야 한다.
본 과제에서 사용한 낱글자에 대해 tesseract는 약 75%의 인식 성공률을 보여주고 있다.

### build_dataset.ipynb

./digits_image 폴더내의 전체화일을 스캔하여 각 이미지를 28x28 픽셀로 조정하고 ndarray 포맷으로 구성하고
npz 포맷으로 저장시킨다.