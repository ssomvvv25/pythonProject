N = int(input())
scores = list(map(int, input().split()))
M = max(scores)
for i in range(len(scores)):
    scores[i] = scores[i]/M*100
Sum = sum(scores)
avg = Sum/len(scores)
print(avg)

#2 - 새로운 리스트 만들어서 풀기
N = int(input())
scores = list(map(int, input().split()))
M = max(scores)

new_scores=[]
for score in scores:
    new_scores.append(score/M*100)
Sum = sum(new_scores)
avg = Sum/len(new_scores)
print(avg)