# 2차원 배열 선언하고 입력받기
# 사이즈는 1<= n <= 15
# 배열을 세로로 읽기

words = [input() for i in range(5)]

for j in range(15):
    for i in range(5):
        if j < len(words[i]):
            print(words[i][j], end='')