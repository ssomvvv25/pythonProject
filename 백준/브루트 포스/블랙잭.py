N,M = map(int, input().split())
arr = list(map(int, input().split()))
max_arr=[]
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1,N):
            three = arr[i] + arr[j] + arr[k]
            if three>M:
                continue # 무시
            else:
                max_arr.append(three)
print(max(max_arr))

# 조합 이용해서 풀기
from itertools import combinations

N,M = map(int, input().split())
arr=list(map(int,input().split()))
max_arr = []

for three in combinations(arr,3):
    if sum(three)>M:
        continue
    else:
        max_arr.append(sum(three))
print(max(max_arr))