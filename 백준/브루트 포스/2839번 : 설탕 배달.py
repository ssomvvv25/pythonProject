N = int(input())
cnt = 0

while N >= 0:
    if N % 5 == 0: # N이 5의 배수이면
        cnt += (N // 5) # 5로 나눈 몫을 구해야 정수
        print(cnt)
        break
    N -= 3
    cnt+=1
else:
    print(-1)

