import sys
input = sys.stdin.readline
n = int(input())
a = []
for i in range(n):
    b = list(input().split())
    a.append(b)
a.sort(key = lambda x : int(x[0]))

for x,y in a:
    print(x,y)


'''
 N
 숫자 정렬 > 사전 정렬
예제 입력 1 
3
21 Junkyu
21 Dohyun
20 Sunyoung
예제 출력 1 
20 Sunyoung
21 Junkyu
21 Dohyun
'''