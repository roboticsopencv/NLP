#sentence

import spacy
spacy.cli.download("en_core_web_sm")
nlp=spacy.load('en_core_web_sm')
str = ''' My name is Tony Stark and I am Iron Man. '''

doc = nlp(str)
for ent in doc:
    print(ent, ent.pos_)