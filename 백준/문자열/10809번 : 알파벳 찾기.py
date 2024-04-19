S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')

#2_for문 이용
S = list(input())
A = 'abcdefghijklmnopqrstuvwxyz'

for i in A:
    if i in S:
        print(S.index(i), end=" ")
    else:
        print('-1', end=" ")