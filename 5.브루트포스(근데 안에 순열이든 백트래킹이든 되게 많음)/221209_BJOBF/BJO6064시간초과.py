import sys
from math import lcm
input = sys.stdin.readline
T = int(input())
for i in range(T): # arr[0] M arr[1] N arr[2] x arr[3] y
    arr = list(map(int,input().split()))
    year,x,y = 0,0,0
    while 1:
        year += 1; x += 1; y += 1
        if x == arr[2] and y == arr[3]:
            print(year)
            break
        if year % arr[0] == 0:
            x = 0
        if year % arr[1] == 0:
            y = 0
        if year > lcm(arr[0], arr[1]) or ((arr[0] == arr[1]) and arr[2] != arr[3]):
            print(-1)
            break
        

'''
(1 ≤ M, N ≤ 40,000, 1 ≤ x ≤ M, 1 ≤ y ≤ N)
예제 입력 1 
3
10 12 3 9
10 12 7 2
13 11 5 6
예제 출력 1 
33
-1
83
'''