# -*- coding: utf-8 -*-
"""plr.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/10x4L4pJE-LUufSs72dbcgX4eozMAMeoW
"""

# Vectorize plr2d
def plr2d_vectorize(X ,T, N):
    #initilize input as np array and convert to row vector
    X=np.array(X)
    if (np.size(X,0) >= np.size(X,1)):
      X=np.transpose(X)

    #initilize weight vector
    W=np.zeros((X.shape[0]+1,1))
    
    # Perceptron learning
    for n in range(0,N,1):
      mismatched=False
      for i in range(T.shape[0]):
        z=np.dot(X[:,i],W[1:])+W[0]
        if z*(T[i]) <= 0:
          mismatched = True
          W[0] = W[0] + (T[i])*1
          W[1] = W[1] + (T[i])*(X[0,i])
          W[2] = W[2] + (T[i])*(X[1,i])
      if mismatched == False:
        print("converged: n=",n)
        break

    print("learning done")
    for i in range(0,T.shape[0]):
      z=np.dot(X[:,i],W[1:])+W[0]
      if z*(T[i]) <= 0:
        print("mismatch[",i,"]")

    return W