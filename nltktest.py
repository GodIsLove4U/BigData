import nltk
from nltk import word_tokenize
##text = word_tokenize("I enjoy biking on the trails")
text = word_tokenize("Pink is my favorite color")
output = nltk.pos_tag(text)
print(output)
