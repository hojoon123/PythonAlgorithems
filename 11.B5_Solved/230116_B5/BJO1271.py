from sys import stdin
input = stdin.readline

n, k = map(int,input().split())
print(n // k)
print(n % k)

'''
예제 입력 1 
1000 100
예제 출력 1 
10
0
'''