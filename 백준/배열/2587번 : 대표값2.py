# 평균, 중앙값(배열로..?)
# 다섯개 수

num=0
nums=[]
sum_nums=0
for i in range(5):
    num = int(input())
    nums.append(num)
    sum_nums = sum(nums)
avg = int(sum_nums/5)
nums.sort()
mid = nums[2]
print(avg)
print(mid)