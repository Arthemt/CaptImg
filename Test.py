import cv2
import numpy as np
from matplotlib import pyplot as plt
import Graham

img1 = cv2.imread('bird1.jpg', 0)
img2 = cv2.imread('bird2.jpg', 0)
img3 = cv2.imread('bird3.jpg', 0)
img4 = cv2.imread('dog1.jpg', 0)
img5 = cv2.imread('dog2.jpg', 0)
img6 = cv2.imread('dog3.jpg', 0)
img7 = cv2.imread('spider1.jpg', 0)
img8 = cv2.imread('spider2.jpg', 0)
img9 = cv2.imread('spider3.jpg', 0)

ret1, th1 = cv2.threshold(img1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret2, th2 = cv2.threshold(img2, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(img3, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret4, th4 = cv2.threshold(img4, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret5, th5 = cv2.threshold(img5, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret6, th6 = cv2.threshold(img6, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret7, th7 = cv2.threshold(img7, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret8, th8 = cv2.threshold(img8, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
ret9, th9 = cv2.threshold(img9, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

image1, contours1, hier1 = cv2.findContours(th1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image2, contours2, hier2 = cv2.findContours(th2, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image3, contours3, hier3 = cv2.findContours(th3, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image4, contours4, hier4 = cv2.findContours(th4, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image5, contours5, hier5 = cv2.findContours(th5, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image6, contours6, hier6 = cv2.findContours(th6, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image7, contours7, hier7 = cv2.findContours(th7, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image8, contours8, hier8 = cv2.findContours(th8, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
image9, contours9, hier9 = cv2.findContours(th9, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

area1 = cv2.contourArea(contours1[0])
area2 = cv2.contourArea(contours2[0])
area3 = cv2.contourArea(contours3[0])
area4 = cv2.contourArea(contours4[0])
area5 = cv2.contourArea(contours5[0])
area6 = cv2.contourArea(contours6[0])
area7 = cv2.contourArea(contours7[0])
area8 = cv2.contourArea(contours8[0])
area9 = cv2.contourArea(contours9[0])

for cnt in contours1:
    hull1 = cv2.convexHull(cnt)
    cv2.drawContours(th1, [hull1], -1, (255, 255, 255), 1)
for cnt in contours2:
    hull2 = cv2.convexHull(cnt)
    cv2.drawContours(th2, [hull2], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull3 = cv2.convexHull(cnt)
    cv2.drawContours(th3, [hull3], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull4 = cv2.convexHull(cnt)
    cv2.drawContours(th4, [hull4], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull5 = cv2.convexHull(cnt)
    cv2.drawContours(th5, [hull5], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull6 = cv2.convexHull(cnt)
    cv2.drawContours(th6, [hull6], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull7 = cv2.convexHull(cnt)
    cv2.drawContours(th7, [hull7], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull8 = cv2.convexHull(cnt)
    cv2.drawContours(th8, [hull8], -1, (255, 255, 255), 1)
for cnt in contours3:
    hull9 = cv2.convexHull(cnt)
    cv2.drawContours(th9, [hull9], -1, (255, 255, 255), 1)


areaA = cv2.contourArea(hull1)
areaB = cv2.contourArea(hull2)
areaC = cv2.contourArea(hull3)
areaD = cv2.contourArea(hull4)
areaE = cv2.contourArea(hull5)
areaF = cv2.contourArea(hull6)
areaG = cv2.contourArea(hull7)
areaH = cv2.contourArea(hull8)
areaI = cv2.contourArea(hull9)

areaA1 = areaA / area1
areaB2 = areaB / area2
areaC3 = areaC / area3
areaD4 = areaD / area4
areaE5 = areaE / area5
areaF6 = areaF / area6
areaG7 = areaG / area7
areaH8 = areaH / area8
areaI9 = areaI / area9
print("bird1 : ",areaA1)
print("bird2 : ",areaB2)
print("bird3 : ",areaC3)
print("dog1 : ",areaD4)
print("dog2 : ",areaE5)
print("dog3 : ",areaF6)
print("spider1 : ",areaG7)
print("spider2 : ",areaH8)
print("spider3 : ",areaI9)

cv2.imshow("Bird1", th1)
cv2.imshow("Bird2", th2)
cv2.imshow("Bird3", th3)
cv2.imshow("dog1", th4)
cv2.imshow("dog2", th5)
cv2.imshow("dog3", th6)
cv2.imshow("spider1", th7)
cv2.imshow("spider2", th8)
cv2.imshow("spider3", th9)

cv2.waitKey()
cv2.destroyAllWindows()
