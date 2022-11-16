import math

a,b,c = map(int,input().split())
result = (c-a)/(a-b) + 1
if (a == c):
    print("1")
    exit()
if (c - a) > (a - b):
    print(math.ceil(result))
else:
    print("2")
    
'''

5 > 5
10 5 15
(c-a)/(a-b) = 
딱 맞을 때만 +1
아니면 + 2 
5 3n >= 5
(c - a) > a - b
15 - 10 10 - 7
5 > 3
5 / 3
15 - 10 + 7 3일
(c - a + b) > c
(c - a + b) / c
12 > 15
a-b > c
(c-a)/(a-b) 
1000 / 70 15
(a-b) * day > c
예제 입력 1 증가,감소,길이
2 1 5 
5 1 6
5 1 5
c - a > a
1 > 5
2일
예제 출력 1 걸리는 일 수
4
2

'''