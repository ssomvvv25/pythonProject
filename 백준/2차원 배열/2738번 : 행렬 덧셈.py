A, B = [], [] # 행렬 초기화

N, M = map(int,input().split()) # 행렬 크기 입력 받기

for row in range(N): # 행렬 A 입력 받기
    row = list(map(int, input().split()))
    A.append(row)
for row in range(N): # 행렬 B 입력 받기
    row = list(map(int, input().split()))
    B.append(row)
# 두 행렬의 같은 위치의 원소를 더한 값을 출력한다.
for row in range(N):
    for col in range(M):
        print(A[row][col] + B[row][col], end=' ') # end=' '를 사용하여 같은 행의 원소들을 공백으로 구분하여 출력한다.
    print() # 각 행의 출력이 끝나면 'print()'를 사용하여 줄바꿈 한다.