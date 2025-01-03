def ngrams(sentences,n):
  words=sentences.lower().split()
  ngrams=[]
  for i in range(len(words)-n+1):
    ngram=tuple(words[i:i+n])
    ngrams.append(ngram)
  return ngrams
sentences="The quick brown fox jumped over the lazy dog"
n=3
print(f"{n}-grams")
ans=ngrams(sentences,n)
for i in ans:
  print(i)
