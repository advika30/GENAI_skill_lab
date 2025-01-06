import numpy as np
def onehot(corpus):
  voc={}
  index=0
  for sentence in corpus:
    words=sentence.lower().split()
    for word in words:
      if word not in voc:
        voc[word]=index
        index+=1
  V=len(voc)
  onehotencode={}
  for word,idx in voc.items():
    onehotvector=np.zeros(V)
    onehotvector[idx]=1
    onehotencode[word]=onehotvector
  return onehotencode,voc
corpus=[
  "I love machine learning",
  "Machine learning is amazing",
  "I love learning new things"
]
e,v=onehot(corpus)
print("vocabulary is",v)
print("one hot encoding is")
for word,idx in e.items():
  print(f"word:'{word} and index'{idx}'")
