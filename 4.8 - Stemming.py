# spell

# Importing required modules
from nltk.stem.porter import PorterStemmer

# Creating the class object
stemmer = PorterStemmer()

# words to stem
words = ['rain', 'raining', 'faith', 'faithful', 'are', 'is', 'care', 'caring']

# Stemming the words
for word in words:
    print(word + ' -> ' + stemmer.stem(word))