#1
N = int(input())
N_list = list(map(int,input().split()))
v = int(input())

print(N_list.count(v))


#2
N = int(input())
N_list = list(map(int,input().split()))
v = int(input())
count = 0

for i in N_list:
    if i == v:
        count +=1
print(count)