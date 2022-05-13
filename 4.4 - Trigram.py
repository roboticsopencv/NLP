#gram

from textblob import TextBlob

# Sample sentence for N-gram detection
sentence = "Technology is best when it brings people together"
ngram_object = TextBlob(sentence)
ngrams = ngram_object.ngrams(n=3) # Computing Bigrams
print(ngrams) 