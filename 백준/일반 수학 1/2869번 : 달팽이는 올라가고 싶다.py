# A = 올라갈 수 있는 거리, B = 미끄러지는 거리, V = 총 거리

import math
A, B, V = map(int, input().split())

day = (V-B) / (A-B)
print(math.ceil(day))