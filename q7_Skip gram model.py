import numpy as np
def skipgram(sentences,wsize):
  voc={}
  index=0
  for s in sentences:
    w=s.lower().split()
    for word in w:
      if word not in voc:
        voc[word]=index
        index+=1
  tp=[]
  for s in sentences:
    w=s.lower().split()
    for i,target_word in enumerate(w):
      start=max(0,i-wsize)
      end=min(len(w),i+wsize+1)
      for j in range(start,end):
        if i!=j:
          context_words=w[j]
          tp.append((target_word,context_words))
  return tp,voc

sentences=[
    "I love machine learning",
    "Machine learning is amazing",
    "I love learning new things"
]
wsize=2
tp,voc=skipgram(sentences,wsize)  
print("vocabulary is",voc,"\n")
print("skip gram is")
for t in tp:
  print(t)
