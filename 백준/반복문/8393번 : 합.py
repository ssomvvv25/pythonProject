n = int(input())
sum = 0 # 변수에 0을 지정
for i in range(1,n+1): # 1부터 n까지
    sum += i # sum = sum + i
print(sum)

# sum함수를 이용한 코드
# print(sum(range(1, int(input())+1)))