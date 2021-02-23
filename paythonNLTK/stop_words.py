from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_text="Hey, My name is iqbal. Do you know about me? Yes, I know you. You come from Bangladesh"
stop_words= set(stopwords.words("English"))
a = word_tokenize(example_text)
print(a)
for word in a:
    if word not in stop_words:
        print(word)