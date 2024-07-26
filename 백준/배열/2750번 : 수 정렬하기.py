# 오름차순 정렬
N = int(input())
arr=[]

for i in range(N):
    num=int(input())
    arr.append(num)
arr.sort()
# print(arr) # [1, 2, 3, 4, 5]

for j in range(len(arr)):
    print(arr[j], sep='/n')