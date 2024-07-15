f=open("d.txt","r")
f1=open("key.txt","w")
words=f.read().split(" ")
word_freq = {}
for word in words:
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1
for word, freq in word_freq.items():
        f1.write(f"{word}: {freq}\n")
f1.close()
