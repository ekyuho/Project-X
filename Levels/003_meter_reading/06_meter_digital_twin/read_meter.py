import cv2
import numpy as np
import matplotlib.pyplot as plt
import pathlib
import sys
import os.path
import pytesseract
import requests
import json
import datetime

s=0

def alarm(msg, channel):
    if channel[0] == 'X': return

    payload = {'text': msg}
    r = requests.post(channel, json=payload)
    print(r.text, msg, channel)

def doit(number, digit5):
    global s
    slack = 'XXhttps://hooks.slack.com/services/T017L20056V/B01JDDMUUJY/PUT YOUR SLACK HOOKUP'
    try:
        with open("meter.current", "r") as f: value = int(f.read())
    except:
        with open("meter.current", "w") as f: f.write(str(number))
        value = number

    print('doit',number,',',value, digit5)

    if number == value:
        #alarm("same meter reading %d.%s"%(number,digit5), slack)
        print("same meter reading %d.%s"%(number,digit5))

        url2 = 'http://54.180.106.144:8080/meter/%d.%s'%(number, digit5[0])
        print(url2)
        r = requests.get(url2)
        print('push to digital_twim', r.text)

        s+=1
    elif number == value+1:
        with open("meter.current", "w") as f: f.write(str(number))

        url2 = 'http://54.180.106.144:8080/meter/%d.%s'%(number,digit5[0])
        print(url2)
        r = requests.get(url2)
        print('push to digital_twim', r.text)


        alarm("meter +1 ok %d.%s"%(number,digit5), slack)
        print("meter +1 ok %d.%s"%(number,digit5))
        s+=1
    else:
        print("Meter wrong %d.%s"%(number,digit5))
        alarm("Meter wrong %d.%s"%(number,digit5), slack)
class OCRError(Exception):
    pass


def get_contours(img):
    # img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #edges = cv2.Canny(img, 20, 60)
    # print('edges:', edges)
    rimg = ~img
    ret, thr = cv2.threshold(rimg, 60, 150, 0)
    contours,_ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # images, contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_LIST)
    return filter_(contours)


def filter_(contours):
    contours_dict = dict()
    for cont in contours:
        x, y, w, h = cv2.boundingRect(cont)
        area = cv2.contourArea(cont)
        if 10 < area and 10 < w and h > 5:
            contours_dict[(x, y, w, h)] = cont
    return sorted(contours_dict.values(), key=cv2.boundingRect)


def to_contours_image(contours, ref_image):
    blank_background = np.zeros_like(ref_image)
    img_contours = cv2.drawContours(blank_background, contours, -1, (255, 255, 255), thickness=2)
    return img_contours


def is_overlapping_horizontally(box1, box2):
    x1, _, w1, _ = box1
    x2, _, _, _ = box2
    if x1 > x2:
        return is_overlapping_horizontally(box2, box1)
    return (x2 - x1) < w1


def merge(box1, box2):
    assert is_overlapping_horizontally(box1, box2)
    x1, y1, w1, h1 = box1
    x2, y2, w2, h2 = box2
    x = min(x1, x2)
    w = max(x1 + w1, x2 + w2) - x
    y = min(y1, y2)
    h = max(y1 + h1, y2 + h2) - y
    return x, y, w, h

def get_windows(contours):
    """return List[Tuple[x: Int, y: Int, w: Int, h: Int]]"""
    boxes = []
    for cont in contours:
        box = cv2.boundingRect(cont)
        if not boxes:
            boxes.append(box)
        else:
            if is_overlapping_horizontally(boxes[-1], box):
                last_box = boxes.pop()
                merged_box = merge(box, last_box)
                boxes.append(merged_box)
            else:
                boxes.append(box)
    return boxes
def to_digit_images(img):
    contours = get_contours(img)
    image_contours = to_contours_image(contours, img)

    windows = get_windows(contours)
    img2 = img.copy()
    for box in windows:
        x, y, w, h = box
        img2 = cv2.rectangle(img2, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #plt.imshow(img2)
    #plt.show()
    if len(windows) != 5:
        raise OCRError
        return []
    else:
        xs = [image_contours[y:y+h, x:x+w] for (x, y, w, h) in windows]
        xs = [img[y:y+h, x:x+w] for (x, y, w, h) in windows]
        return xs

def conv(img, n):
    #print('conv',n)
    kernel = np.ones((n,n),np.float32)/(n*n)
    return cv2.filter2D(img, -1, kernel)

def blur(img, method):
    if method == "blur": return cv2.blur(img,(7,7))
    if method == "median": return cv2.medianBlur(img,9)
    if method == "bilateral": return cv2.bilateralFilter(img,9,75,75)
    if method == "gaussian": return cv2.GaussianBlur(img,(5,5),8)

def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = requests.get(url)
    print(resp.status_code)
    image = np.asarray(bytearray(resp.content), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    # return the image
    return image

def file2files(fpath):
    plt.figure(figsize=(20,20))
    #img = cv2.imread(fpath, cv2.IMREAD_GRAYSCALE)
    img = url_to_image('http://54.180.106.144:8080/websensor')
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    plt.subplot(1,5,1)
    plt.imshow(img)
    plt.xlabel('org')
    #print('shape=', img.shape)
    M = cv2.getRotationMatrix2D((130, 400), -27, 1.0)
    img = cv2.warpAffine(img, M, (1280, 720))

    plt.subplot(1,5,2)
    plt.imshow(img)
    plt.xlabel('rotate')
    #cv2.imwrite('x.jpg', img)

    pts1 = np.float32([[138,432],[167,521],[708,407],[709,517]])
    pts2 = np.float32([[140,430],[140,520],[706,430],[706,520]])
    M = cv2.getPerspectiveTransform(pts1, pts2)
    img = cv2.warpPerspective(img, M, (1280, 728))
    plt.subplot(1,5,3)
    plt.imshow(img)
    plt.xlabel('deform')
    #cv2.imwrite('x.jpg', img)

    img = img[406:536,120:730]
    plt.subplot(1,5,4)
    plt.imshow(img)
    plt.xlabel('crop')

    img = blur(conv(img,5), "bilateral")
    plt.subplot(1,5,5)
    plt.imshow(img)
    plt.xlabel('blur')

    rois = to_digit_images(img)
    plt.figure(figsize=(20,20))
    number=[]
    for i, digit_img in enumerate(rois):
        #outfilepath = fpath.with_name(fpath.stem + ('_%d' % i) + '.png')
        #cv2.imwrite(outfilepath.as_posix(), digit_img)
        rd = ~digit_img
        plt.subplot(1,5,i+1)
        plt.imshow(rd)
        n = str(pytesseract.image_to_string(rd, config='--oem 3 --psm 10 -c tessedit_char_whitelist=0123456789'))
        n = n[0:-2]
        number.append(n)
        print('n=', n)
        if n == ' ': plt.xlabel('blank')
        else: plt.xlabel(n)
        if not n.isnumeric():
            d = datetime.datetime.now()
            fname = "%s_%s.jpg"%(d.strftime("%Y-%m-%d-%H:%M:%S"),n)
            print('save n', 'AIFail/'+fname)
            cv2.imwrite('AIFail/'+fname, rd)
    num = ''.join(number[0:4])
    if num.isnumeric():
        meter = int(num)
        doit(meter, number[4])
    else:
        print("meter wrong=", num)

    plt.show()

if __name__ == "__main__":
    file = '2021-01-08_0000.jpg'
    if len(sys.argv)>1: 
        file = sys.argv[1]
        if not os.path.isfile(file): print('nofile', file)
    else:
        file2files(file)

