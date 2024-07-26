N = int(input())

num = 666
cnt = 0

while True:
    if '666' in str(num): # N번째 수에 '666'이 포함되어 있다면 (str이 아니면 무조건 1의자리부터 시작하니까)
        cnt +=1 # 카운트하기
    if cnt == N: # 카운트랑 N이 같다면
        print(num) # num을 출력하고
        break # while문 종료
    num+=1 # 666이 포함된 수가 나올 때까지 num을 1씩 증가 시킨다