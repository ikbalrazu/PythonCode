#from nltk.corpus import treebank
#t=treebank.parsed_sents('wsj_0001.mrg')[0]
#t.draw()

from nltk.tokenize import word_tokenize, sent_tokenize


sentence ="Hello there, i am iqbal. I want to show you something. But before! you give me some paper for proof this. Do you want to do that?"
wt=word_tokenize(sentence)
st=sent_tokenize(sentence)
print('Here is the word tokenize:',wt)
print('Here is the sent tokenize:',st)

from nltk.stem import PorterStemmer
pst=PorterStemmer()
pr=pst.stem("want to")
print(pr)


