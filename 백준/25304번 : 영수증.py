x = int(input())
n = int(input())
total = 0 # 초기화
for i in range(1, n+1):
    a, b = map(int, input().split())
    total += a*b # 이 부분에서 틀렸었음!!
if x == total:
    print('Yes')
else:
    print('No')