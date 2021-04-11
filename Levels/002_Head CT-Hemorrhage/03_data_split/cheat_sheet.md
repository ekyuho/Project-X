{"target":"mento", "type":"mission","id":"3","description":"data split"}
## 데이터 구분
학습을 위해 데이터를 train 80%, validation 10%, test 10%로 나누어라.
## 키워드
train_test_split

## 평가
* 데이터를 train, validation, test로 나누었는가? (train_test_split을 사용하지 않았어도 감점 요소가 아님)
* 퀴즈1: train_test_split을 사용할 때, 실행 시 마다 같은 학습 데이터를 얻고 싶다. 어떤 인자 값을 어떻게 해야 하는가?
* 정답1: random_state에 임의의 값을 넣어준다. 시드를 고정하기 때문에 실생 시마다 같은 학습 데이터를 얻는다.
