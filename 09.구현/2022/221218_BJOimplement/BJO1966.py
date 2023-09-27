import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N, target = map(int,input().split())
    level = list(map(int, input().split( )))
    arr = [0 for i in range(N)]
    arr[target] = 'target'
    order = 0
    
    while 1:
        if level[0] == max(level):
            order += 1
            if arr[0] == 'target':
                print(order)
                break
            else:
                level.pop(0)
                arr.pop(0)
        
        else:
            level.append(level.pop(0))
            arr.append(arr.pop(0))

'''
T
N(1 ≤ N ≤ 100), M(0 ≤ M < N)

예제 입력 1 
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
예제 출력 1 
1
2
5
'''