from PIL import Image
import pytesseract
import io
from wand.image import Image as wi 


'''
##Teste com a imagem

image = Image.open("sample1.jpg")

text = pytesseract.image_to_string(image, lang = 'eng')

print(text)
'''

##Teste com .pdf

pdf = wi(filename = "CV_GuilhermeCPereira.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'eng')
	recognized_text.append(text)

print(recognized_text)