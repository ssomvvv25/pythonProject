num = []

for i in range(10):
    remain = int(input())%42
    if remain not in num:
        num.append(remain)
print(len(num))