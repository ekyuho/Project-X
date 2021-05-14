{"type":"mission","id":"3","description":"get number via calling google tesseract with image"}
## Reconize digit image by calling Google tesseract

### Google tesseract 활용 사례

```
n = pytesseract.image_to_string(img, config='--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789')
plt.xlabel(n)
plt.imshow(rd)
```

![인식결과](image4.jpg)

인식된 값을 X축의 레이블로하여 그림으로 표현하였다.
282는 잘 인식되었으나, 0과 4는 인식되지 않았음을 알 수 있다.

04_build_training_dataset 미션 디렉토리에 다음과 같은 2개의 디렉토리가 있다.

  ./digits_image
  ./meter_image
  
./meter_image에 저장된 3082개의 계량이 이미지로부터 숫자를 5개씩 추출해서 낱글자로 위의 프로그램을 통해 얻은 문자인식 결과는 다음과 같다.

 * 계량이 이미지 3082개
 * 추출되어 사용된 낱글자 이미지 14,864개
 * 다음은 낱자별로 tesseract에서 empty string을 리턴한 케이스
 
  글자 | 건수
  ----|----
  0 | 2802
  1 | 242
  2 | 33
  3 | 82
  4 | 90
  5 | 48
  6 | 92
  7 | 206
  8 | 284
  43 | 9