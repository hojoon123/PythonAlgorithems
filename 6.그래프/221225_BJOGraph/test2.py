from sys import stdin
input = stdin.readline

x,y,w,h = map(int,input().split())
print(min(x,y,w-x,h-y))
'''
6 2 10 3
예제 출력 1 
1
예제 입력 2 
1 1 5 5
예제 출력 2 
1
'''