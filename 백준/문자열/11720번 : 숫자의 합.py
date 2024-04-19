N = input()
print(sum(map(int,input())))

#2_for문 이용(1)
N = input()
nums = input()
total = 0
for i in nums:
    total += int(i) # total = total + int(i)
print(total)

#3_for문 이용(2)
N = int(input())
nums = input()
total = 0
for i in range(N):
    total += int(nums[i])
print(total)