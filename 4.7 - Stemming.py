# snow

from nltk.stem import SnowballStemmer

st = SnowballStemmer("english")
text = ['Where did he learn to dance like that?',
        'His eyes were dancing with humor.',
        'She shook her head and danced away',
        'Alex was an excellent dancer.']

output = []
for sentence in text:
    output.append(" ".join([st.stem(i) for i in sentence.split()]))

for item in output:
    print(item)

print("-" * 50)
print(st.stem('jumping'), st.stem('jumps'), st.stem('jumped'))