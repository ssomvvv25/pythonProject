# 약수들 다 더했을 때 n이면 완전수. 아니면 'is NOT perfect'

while True:
    n = int(input())
    if n == -1:
        break;
    nums = []
    for i in range(1, n):
        if n % i == 0:
            nums.append(i)
    if sum(nums) == n:
        print(n,' = '," + ".join(str(i) for i in nums), sep="")
    else:
        print(n, "is NOT perfect.")