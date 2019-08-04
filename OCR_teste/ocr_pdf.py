##Libs para o OCR
from PIL import Image
import pytesseract
import io
from wand.image import Image as wi
##Libs para Analise das palavras
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
##Libs Gerais
import random
import pickle
from collections import Counter 
import pandas as pd 
import numpy as np 


'''
##Teste com a imagem

image = Image.open("sample1.jpg")

text = pytesseract.image_to_string(image, lang = 'eng')

print(text)


##Teste com .pdf
'''
pdf = wi(filename = "CV_GuilhermeCPereira.pdf", resolution = 300)
pdfImage = pdf.convert('jpeg')

imageBlobs = []

for img in pdfImage.sequence:
	imgPage = wi(image = img)
	imageBlobs.append(imgPage.make_blob('jpeg'))

recognized_text = []

for imgBlob in imageBlobs:
	im = Image.open(io.BytesIO(imgBlob))
	text = pytesseract.image_to_string(im, lang = 'por')
	recognized_text.append(text)

arrayPalavras = np.array(recognized_text)

np.savetxt('arrayPalavras.txt', arrayPalavras, fmt='%s')



print("Arquivo salvo...\n\n")

###Monatndo o lexicon

lemmatizer = WordNetLemmatizer()

dic = []

with open('arrayPalavras.txt', 'r') as f:
	conteudo = f.readlines();
	for l in conteudo[:53]:
		palavras = word_tokenize(l)
		dic += list (palavras)

dic = [lemmatizer.lemmatize(i) for i in dic]


##Filtrando as palavras
palavras_ruido = set(stopwords.words('portuguese'))

filter_dic = [w for w in dic if not w in palavras_ruido]

print("Tamanho do dicionario inicial\t")
print(len(filter_dic))

for word in filter_dic:
	print(word)
'''

O tamanho do dicionario incial ja é pequeno 
não é possível excluir informação e a mesma continuar relevante

##Exluindo palavras que se repetem muito
cont_palavras = Counter(dic)

WOI = [] ##Words of Intested

for palavra in cont_palavras:
	if 5 > cont_palavras[palavra] > 1:
		WOI.append(palavra)


print("\nTamanho do dicionario de palavras\t")
print(len(WOI))
print("\n Palavras presentes do dicionario\n")
print(WOI)
'''

