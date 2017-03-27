import cv2
import numpy as np
from math import pow, fabs, sin
from random import randrange
import sys

def f1(x, y):
    return (x+y)

def f2(x, y, q):
    return abs(sin(x/q)*y)

def f3(x, y):
    return (pow(x/q, 2)+2*pow(y/q, 2))

def f4(x, y):
    return randrange(256)

filename = input()
n = int(input())
function = input()
q = input()

sys.stdout.write("What I got!\n")
sys.stdout.write("Filename: " + filename + "\n")
sys.stdout.write("N: " + str(n) + "\n")
sys.stdout.write("Function: " + function + "\n")
sys.stdout.write("Q: " + q + "\n\n\n")

# for x in range(n):
#     for y in range(n):
#         res = f1(x, y)
#         print(res)

img = np.zeros((n, n, 1), np.uint8)
cv2.imwrite("img-black.jpg", img)

for x in range(n):
    for y in range(n):
        img[x, y] = f1(x, y)

cv2.imwrite("img-grey.jpg", img)
