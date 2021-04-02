from pytesseract import pytesseract
import cv2
import re

path_to_tesseract=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
pytesseract.tesseract_cmd=path_to_tesseract

text=pytesseract.image_to_string(cv2.imread('im1.jpg'), config='-l eng --oem 1 --psm 3')



m = re.findall(r"(?i)Name : [\w]+ [\w]+", text)
print(m)

# You can give three important flags for tesseract to work and these are -l , --oem , and --psm.

# The -l flag controls the language of the input text.

# The --oem argument, or OCR Engine Mode, controls the type of algorithm used by Tesseract.

# The --psm controls the automatic Page Segmentation Mode used by Tesseract.