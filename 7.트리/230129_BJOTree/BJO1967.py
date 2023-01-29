import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def preorder(root, ans, direction):
    global left_max, right_max
    if root == 0:
        return
    ans += biased[root]
    preorder(tree[root][0], ans, direction)
    preorder(tree[root][1], ans, direction)
    if direction == 0: # left
        if ans > left_max:
            left_max = ans

    if direction == 1: # right
        if ans > right_max:
            right_max = ans

    

if __name__ == '__main__':
    n = int(input())
    tree = [[0] * 2 for i in range(n + 2)]
    biased = [0, 0]
    left_max = 0
    right_max = 0
    for i in range(n - 1):
        root, child, biase = map(int,input().split())
        if tree[root][0] == 0:
            tree[root][0] = child
        else:
            tree[root][1] = child
        biased.append(biase)
        
    preorder(tree[1][0], 0, 0)
    preorder(tree[1][1], 0, 1)
    print(left_max + right_max + 2)
    
'''
dfs를 두번 돌려서 
왼쪽 서브트리 오른쪽 서브트리를 나눠서 제일 긴 값을 더 하고 노드값 +2 를 해줬음
구현에는 성공했으나 6퍼센트에서 틀림
43인데 45라고 나오길래 노드값도 포함인가 해서 2 더해보니까 딱 맞길래 
멍청하게 바로 해버렸음.
조금만 생각해봐도 오른쪽에서 2개가 나올 수도 있는 건데 너무 성급했음.
예제 입력 1 
12
1 2 3
1 3 2
2 4 5
3 5 11

3 6 9
4 7 1
4 8 7
5 9 15

5 10 4
6 11 6
6 12 10

예제 출력 1 
45
'''