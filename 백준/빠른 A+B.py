import sys

T = int(sys.stdin.readline())
for i in range(T):
    A,B = map(int, sys.stdin.readline().split())
    print(A+B)


"""
#2
T = int(input())
for i in range(T):
    a,b = map(int, sys.stdin.readline().split()) # 여기가 포인트
    print(a+b)
"""