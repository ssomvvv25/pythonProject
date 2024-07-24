# 2차원 배열 선언
array = [[0 for col in range(9)] for row in range(9)]

# 2차원 배열 입력받기
for i in range(9):
    array[i] = list(map(int, input().split()))

# 최댓값과 그 값의 위치 찾기
max_num = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if max_num <= array[row][col]:
            max_row, max_col = row+1, col+1
            max_num = array[row][col]
print(max_num)
print(max_row, max_col)



