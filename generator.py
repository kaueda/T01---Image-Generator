# Student: Kaue Ueda Silveira
# NUSP: 7987498

import cv2
import sys
import numpy as np
from random import randrange
from math import pow, fabs, sin

def f1(x, y, q):
    return (x+y)

def f2(x, y, q):
    return fabs(sin(x/q)*255)

def f3(x, y, q):
    return (pow(x/q, 2)+2*pow(y/q, 2))*255

def f4(x, y, q):
    return randrange(256)

func_options = {
    'f(1)' : f1,
    'f(2)' : f2,
    'f(3)' : f3,
    'f(4)' : f4,
}

# 1. Parameter Input
filename = input()
n = int(input())
function = input()
q = int(input())

img = cv2.imread(filename.strip(), cv2.IMREAD_GRAYSCALE)
if img is None:
    print("Could not load image: " + filename)
    img = np.zeros((n, n, 1), np.uint8)

# 2. Generate image
for x in range(n):
    for y in range(n):
        img[x, y] = func_options[function.strip()](x, y, q)

# 3. Show Image
cv2.imshow("show image", img)

# 3. Store image as png
cv2.imwrite(filename.split('.')[0] + ".png", img)

