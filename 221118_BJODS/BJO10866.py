import sys
input = sys.stdin.readline

arr = []
for _ in range(int(input())):
    a = list(input().split())
    order = a[0]
    
    if order == 'push_front':
        arr.insert(0,a[1])
        
    elif order == 'push_back':
        arr.append(a[1])
        
    elif order == 'pop_front':
        if arr : print(arr.pop(0))
        else : print(-1)
        
    elif order == 'pop_back':
        if arr : print(arr.pop())
        else : print(-1)
        
    elif order == 'size':
        print(len(arr))
        
    elif order == 'empty':
        if arr : print(0)
        else : print(1)
        
    elif order == 'front':
        if arr : print(arr[0])
        else : print(-1)
        
    elif order == 'back':
        if arr : print(arr[-1])
        else : print(-1)


'''
예제 입력 1 
15
push_back 1
push_front 2
front
back
size
empty
pop_front
pop_back
pop_front
size
empty
pop_back
push_front 3
empty
front
예제 출력 1 
2
1
2
0
2
1
-1
0
1
-1
0
3
'''