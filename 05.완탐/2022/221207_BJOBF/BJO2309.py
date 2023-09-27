import sys
from math import sqrt
input = sys.stdin.readline
N = [] 
[N.append(int(input())) for i in range(9)]
tmp = 0; tmp2 = 0
for i in range(9):
    for j in range(i+1,9):
        if sum(N) - (N[i] + N[j]) == 100:
            tmp = N[i] 
            tmp2 = N[j]
            
N.remove(tmp) 
N.remove(tmp2)
N.sort()
for i in range(7): print(N[i])
        
    
'''
예제 입력 1 
20
7
23
19
10
15
25
8
13
예제 출력 1 
7
8
10
13
19
20
23
'''