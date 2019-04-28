import pandas as pd
import numpy as np 
from PIL import Image
import pytesseract

image = Image.open("sample1.jpg")

text = pytesseract.image_to_string(image, lang = 'eng')

print(text)
