import numpy as np

N,X = map(int,input().split())
N_list = list(map(int,input().split()))
X_list = []
for i in N_list:
    if i < X:
        np.append(X_list,i)
    print(X_list)