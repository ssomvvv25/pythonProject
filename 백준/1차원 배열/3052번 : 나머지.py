num = [int(input()) for _ in range(10)]
remain = set()

for i in num:
    rem = i % 42
    remain.add(rem)

print(len(remain))

#2
num = []

for i in range(10):
    remain = int(input())%42
    if remain not in num:
        num.append(remain)
print(len(num))