import cv2
import numpy as np
from matplotlib import pyplot as plt
import Graham

img = cv2.imread('main.jpg', 0)
ret, th1 = cv2.threshold(img, 10, 255, 0)


