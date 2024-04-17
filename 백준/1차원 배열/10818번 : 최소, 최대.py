#1
N = int(input())
A = list(map(int, input().split()))

Max = max(A)
Min = min(A)

print(Min, Max)

#2 위에 있는 코드를 더 간단하게 : max(),min()함수 쓸 때 굳이 치환 안 해도 됨!
N = int(input())
A = list(map(int, input().split()))
print(min(A), max(A))

#3
N = int(input())
A = list(map(int, input().split()))
Max = A[0]
Min = A[0]

for i in A[1:]:
    if i > Max:
        max = i
    elif i < Min:
        min = i
print(Min, Max)
