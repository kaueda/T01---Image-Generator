# Student: Kaue Ueda Silveira
# NUSP: 7987498

import cv2
import numpy as np
import sys

filename = input()
n = int(input())
function = input()
q = int(input())

img = cv2.imread(filename)
if img is None:
	print("Could not load image")

