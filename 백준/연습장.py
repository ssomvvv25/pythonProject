T = int(input())
for i in range(T): # 입력 받은 테스트 케이스의 개수만큼 반복한다.
    R,S = input().split() # 공백을 기준으로 입력 받는다.
    for j in range(len(S)): # 문자열 S의 각 문자에 대해 반복한다.
        print(int(R)*S[j],end='') # 문자열S의 각 문자를 반복 횟수 R만큼 곱하여 출력한다.
    print('')
