from sys import stdin
input = stdin.readline

res = 1
for i in range(3): # res 에 곱하는 연산을 빼는 편이 이득 줄이 늘어나고 연산량을 줄일 수 있는 상황
    n = int(input())
    res *= n
res = list(str(res))

for i in range(10):
    print(res.count(str(i)))
    
'''
예제 입력 1 
150
266
427
예제 출력 1 
3
1
0
2
0
0
0
2
0
0
'''