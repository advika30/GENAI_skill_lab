import numpy as np
def softmax(x,axis=-1):
  x_exp=np.exp(x-np.max(x,axis=axis,keepdims=True))
  return x_exp/np.sum(x_exp,axis=axis,keepdims=True)
def self_attention(x,wq,wk,wv):
  q=np.dot(x,wq)
  k=np.dot(x,wk)
  v=np.dot(x,wv)
  d_k=q.shape[1]
  score=np.dot(q,k.T)/np.sqrt(d_k)
  wt=softmax(score,axis=-1)
  output=np.dot(wt,v)
  return output
np.random.seed(0)
x=np.random.rand(4,3)
d=3
d_out=2
wq=np.random.rand(d,d_out)
wk=np.random.rand(d,d_out)
wv=np.random.rand(d,d_out)
output=self_attention(x,wq,wk,wv)
print(output)
print(wq)
print(wk)
print(wv)
