import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    q = deque()
    q.append((a,""))
    while q:
        num, path = q.popleft()
        visit[num] = True
        if num == b:
            print(path)
            break
        

        next = (2*num)%10000
        if not visit[next]:
            q.append((next,path+"D"))
            visit[next] = True

        next = (num-1)%10000
        if not visit[next]:
            q.append((next,path+"S"))
            visit[next] = True
            
        next = (10*num+(num//1000))%10000
        if not visit[next]:
            q.append((next,path+"L"))
            visit[next] = True
            
        next = num//10+(num%10)*1000
        if not visit[next]:
            q.append((next,path+"R"))
            visit[next] = True
    


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = map(int,input().split())
        visit = [False] * 10000
        bfs(n,m)

'''
예제 입력 1 
3
1234 3412
1000 1
1 16
예제 출력 1 
LL
L
DDDD
'''