import cv2
import pytesseract
import matplotlib.pyplot as plt

img = cv2.imread('imgs/test6.png')
img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
gray = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
img = cv2.merge([gray,gray,gray])

plt.imshow(img)
plt.show()

cfg = "digits"
# # Распознавание, допустимы только цифры
balance = pytesseract.run_and_get_output(img, extension='txt', config=cfg)
print(balance)

