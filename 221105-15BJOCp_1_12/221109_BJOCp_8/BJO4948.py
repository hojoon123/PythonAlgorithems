import sys
from math import sqrt
input = sys.stdin.readline
def func(n):
    result = 0
    for j in range(2,int(sqrt(i)) + 1): #i-1 까지임
        if i % j == 0:
            break
    else:
        result += 1
    return result

arr = list(range(2,246912))
resultArr = []

for i in arr:
    if func(i):
        resultArr.append(i)
        
while 1 :
    cnt = 0
    a = int(input())
    if(a == 0):
        break
    for i in resultArr:
        if(a < i <= a *2):
            cnt+=1

    print(cnt)

''' 
예제 입력 1 
1
10
13
100
1000
10000
100000
0
예제 출력 1 
1
4
3
21
135
1033
8392

'''