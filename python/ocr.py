import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import os
import pandas as pd
import numpy as np


rootdir = "."
regex = re.compile('.*.png')

U = [[]]

# for root, dirs, files in os.walk(rootdir):
#   for file in files:
#     if regex.match(file):

img = cv2.imread('test.png')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
img = cv2.merge([gray,gray,gray])

img = img[:,0:img.shape[0]//2,:]
# plt.imshow(img)
# plt.show()

cfg = "digits"
# # Распознавание, допустимы только цифры
digits = pytesseract.run_and_get_output(img, extension='txt', config=cfg).split()
for i, digit in enumerate(digits):
    if digit[0] == '0':
        digits[i] = digit[0] + '.' + digit[1:]

    U[-1].append(float(digits[i]))

U = np.array(U).T

df = pd.DataFrame({'in': U[0], 'out': U[1], 'out_mean': U[2]})
df.to_excel('task4.xlsx', index=False)


