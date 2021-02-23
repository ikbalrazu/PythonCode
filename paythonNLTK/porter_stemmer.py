from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

port=PorterStemmer()
example_text = "I used my computer. I have been useing it. I use this computer everyday"
for i in word_tokenize(example_text):
    print(port.stem(i))