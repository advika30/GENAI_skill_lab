import numpy as np
def rnn_forward(x,wxh,whh,why,bh,by,h0):
  h=h0
  hs=[]
  ys=[]
  for t in range(len(x)):
   xt=np.array([[x[t]]])
   h=np.tanh(np.dot(whh,h)+np.dot(wxh,xt)+bh)
   y=np.dot(wxy,h)+by
   hs.append(h)
   ys.append(y)
  return hs,ys
x=[1,2,3]
np.random.seed(0)
i=1
hsize=4
o=1
wxh=np.random.rand(hsize,i)*0.01
whh=np.random.rand(hsize,hsize)*0.01
why=np.random.rand(o,hsize)*0.01
bh=np.zeros((hsize,1))
by=np.zeros((o,1))
h0=np.zeros((hsize,1))
h,y=rnn_forward(x,wxh,whh,why,bh,by,h0)
for t,y in enumerate(y):
  print(f"time:{t+1} y={y.flatten()}")
