import sys
input = sys.stdin.readline

arr = [1 for i in range(1000001)]
arr[2] = 2; arr[3] = 4
for i in range(4,1000001):
    arr[i] = arr[i-1] % 1000000009 + arr[i-2] % 1000000009 + arr[i-3] % 1000000009
for _ in range(int(input())):
    n = int(input())
    print(arr[n] % 1000000009) 

'''
T (1 <= N <=  1,000,000)
1000000009
예제 입력 1 
3
4
7
10
예제 출력 1 
7
44
274
'''