{"type":"mission","id":"3","description":"get number via calling google tesseract with image"}
## Reconize digit image by calling Google tesseract

### 1. Call Google tesseract

```
n = pytesseract.image_to_string(img, config='--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789')
plt.xlabel(n)
plt.imshow(rd)
```

![인식결과](image4.jpg)

인식된 값을 X축의 레이블로하여 그림으로 표현하였다.
282는 잘 인식되었으나, 0과 4는 인식되지 않았음을 알 수 있다.