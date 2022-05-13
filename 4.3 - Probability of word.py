#count

from nltk.corpus import brown
from nltk.tokenize import word_tokenize

corpus=brown.words()
lower_case_corpus=[w.lower() for w in  corpus]
vocab=set(lower_case_corpus)
print('corpus Example:' + str(lower_case_corpus[:30]))
"""print('vocab Example:' + str(list(vocab)[:10]))
print('total in corpus :' + str(len(lower_case_corpus)))
print('vocab of the corpus :' + str(len(vocab)))"""
bigram_count={}
trigram_count={}
for i in range(len(lower_case_corpus)-2):
    bigram=(lower_case_corpus[i],lower_case_corpus[i+1])
    trigram=(lower_case_corpus[i],lower_case_corpus[i+1],lower_case_corpus[i+2])
    if bigram in bigram_count.keys():
        bigram_count[bigram]+=1
    else:
        bigram_count[bigram] = 1
    if trigram in trigram_count.keys():
        trigram_count[trigram]+=1
    else:
        trigram_count[trigram] = 1
print("Example,Count for bigram('the','fulton') is:"+str(bigram_count[('the','fulton',)]))

def suggest_next_word(input,bigram_count,trigram_count,vocab):
    tokenized_input=word_tokenize(input.lower())
    last_bigram=tokenized_input[-2:]
    vocab_probabilities={}
    for vocab_word in vocab:
        test_trigram=(last_bigram[0],last_bigram[1],vocab_word)
        test_bigram=(last_bigram[0],last_bigram[1])
        test_trigram_count=trigram_count.get(test_trigram,0)
        test_bigram_count=bigram_count.get(test_bigram,0)
        probability=test_trigram_count/test_bigram_count
        vocab_probabilities[vocab_word]=probability

    top_suggesstions=sorted(vocab_probabilities.items(),key=lambda x:x[1],reverse=True)[:3]
    print(top_suggesstions)

suggest_next_word('the fulton county',bigram_count,trigram_count,vocab)
