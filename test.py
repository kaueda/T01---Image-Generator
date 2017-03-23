import cv2
import numpy as np
import sys

def f1(x, y):
    return x+y

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
cv2.imshow("img black", img)
cv2.waitKey(0)

for x in range(n):
    for y in range(n):
        img[x, y] = [f1(x, y)]

cv2.imshow("img grey", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
