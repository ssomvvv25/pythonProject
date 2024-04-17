A = [] # 빈 리스트 생성
for _ in range(9):
    i = int(input())
    A.append(i)
print(max(A))
print(A.index(max(A))+1)

# 리스트 컴프리헨션 사용
A = [int(input()) for _ in range(9)]
print(max(A))
print(A.index(max(A))+1)