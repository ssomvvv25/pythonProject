word = input().upper() # 입력된 단어를 모두 대문자로 변환하여 저장
word_list = list(set(word)) # 중복을 제거한 단어 리스트를 생성 *set자료형은 중복을 허용하지 않으므로 이를 이용해 중복을 제거한다.

cnt = []
for i in word_list:
    count = word.count # count메서드를 변수로 할당
    cnt.append(count(i)) # 해당 알파벳의 개수를 cnt 리스트에 추가

if cnt.count(max(cnt)) > 1:
    print("?")
else:
    print(word_list[cnt.index(max(cnt))]) # 가장 많이 사용된 알파벳 출력