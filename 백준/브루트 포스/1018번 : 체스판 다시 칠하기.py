# i, i+1 : 둘이 같으면 바꿔...... i+1을 . ..
# 원래의 체스판 = 8X8!!
N, M = map(int, input().split())

original = [] # 원래 첼스판
new = [] # 바뀐 체스판

for _ in range(N):
    original.append(input())
