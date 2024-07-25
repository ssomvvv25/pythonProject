# 소수 = 약수가 1과 자기자신뿐 => 약수의 개수가 2개여야만 함
N = int(input())
nums = list(map(int, input().split()))
cnt = 0 # 소수 갯수

for num in nums:
    if num == 1: # 1은 소수가 아님
        continue
    for x in range(2, num):
        if(num % x ==0):
            break
    else:
        cnt +=1
print(cnt)

