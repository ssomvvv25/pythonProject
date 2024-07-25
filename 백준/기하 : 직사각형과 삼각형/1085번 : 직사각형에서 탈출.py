x,y,w,h = map(int,input().split())

# 직사각형의 경계선에 가는 거리 <- 오른쪽 위 꼭짓점을 말하는게  아님
print(min(x,y,w-x,h-y))