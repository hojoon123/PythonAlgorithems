import sys
input = sys.stdin.readline
s = []

for _ in range(int(input())):
    a = list(input().split())
    order = a[0]
    
    if order == 'push':
        s.insert(0,a[1])
    elif order == 'pop':
        if s : print(s.pop())
        else : print(-1)
    elif order == 'size':
        print(len(s))
    elif order == 'empty':
        if s : print(0)
        else : print(1)
    elif order == 'front':
        if s : print(s[-1])
        else : print(-1)
    elif order == 'back':
        if s : print(s[0])
        else : print(-1)


'''
예제 입력 1 
15
push 1
push 2
front
back
size
empty
pop
pop
pop
size
empty
pop
push 3
empty
front
예제 출력 1 
1
2
2
0
1
2
-1
0
1
-1
0
3
'''