#1
word = list(input())
if word == word[::-1] :
    print(1)
else:
    print(0)

#2
word = list(input())
word_reverse = list(reversed(word))

if word == word_reverse:
    print(1)
else:
    print(0)