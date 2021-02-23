from nltk.tokenize import word_tokenize,sent_tokenize

example_text="Hello there, My name is iqbal. I come from Bangladesh? I am living here have been last five years."
print(sent_tokenize(example_text))
print(word_tokenize(example_text))
for i in sent_tokenize(example_text):
    print(i)

for n in word_tokenize(example_text):
    print(n)

import nltk
from nltk import ne_chunk
def postag():
    wordtokenize=word_tokenize(example_text)
    pos_tagNow = nltk.pos_tag(wordtokenize)
    pos_tagChunk=ne_chunk(pos_tagNow)
    print(pos_tagChunk)
    print(len(wordtokenize))

#call all methods
postag()


