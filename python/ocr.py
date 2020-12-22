import cv2
import pytesseract
import matplotlib.pyplot as plt
import re
import os
import pandas as pd
import numpy as np


rootdir = "task4"
regex = re.compile('.*out.png')

U = [[]]

listfiles = []
for root, dirs, files in os.walk(rootdir):
  for file in files:
    if regex.match(file):
        listfiles.append(os.path.join(rootdir,file))

listfiles = np.sort(listfiles)
# listfiles = listfiles[0:10]

U = np.full((len(listfiles), 3), None)

for j, file in enumerate(listfiles):
    img = cv2.imread(file)

    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    gray = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
    img = cv2.merge([gray,gray,gray])

    img = img[:,0:img.shape[0]//2,:]


    cfg = "digits"
    # # Распознавание, допустимы только цифры
    digits = pytesseract.run_and_get_output(img, extension='txt', config=cfg).split()

    if digits[0][0] == '0':
        digits[0] = digits[0][0] + '.' + digits[0][1:]

    print(digits)
    for i, digit in enumerate(digits):
        U[j,i] = digits[i]

U = np.array(U).T
df = pd.DataFrame({'in': U[0], 'out': U[1], 'out_mean': U[2]})
print(df)
df.to_excel('task4.xlsx', index=False)


