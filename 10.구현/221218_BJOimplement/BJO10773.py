import sys
input = sys.stdin.readline

N = int(input())
arr = []
for i in range(N):
    num = int(input())
    if num == 0:
        arr.pop()
    else:
        arr.append(num)
print(sum(arr))
'''
(1 ≤ K ≤ 100,000)
예제 입력 1 
4
3
0
4
0
예제 출력 1 
0
10
1
3
5
4
0
0
7
0
0
6
'''