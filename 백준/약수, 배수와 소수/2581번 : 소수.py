M = int(input())
N = int(input())

sosu = [] # 소수
for num in range(M,N+1): # M이상 N이하
    cnt = 0 # 소수가 아니면 카운트
    if num > 1: # 2이상의 수들 중에서 소수를 찾는다.
        for x in range(2, num): # 2~num에서 나눠지는 수를 찾는다.
            if (num % x ==0): # 나머지가 0이면 소수 아님
                cnt +=1
                break
        if cnt == 0: # cnt = 0일 때 : 나눠지는 수가 없을 때! => 소수
            sosu.append(num)
if len(sosu) > 0:
    print(sum(sosu))
    print(min(sosu))
else:
    print('-1')