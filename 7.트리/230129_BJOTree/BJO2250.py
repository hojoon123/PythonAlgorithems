import sys
import itertools
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)


def inorder(root, level):
    global location
    if root != -1:
        inorder(tree[root][0], level + 1)
        row[level].append(location)
        location += 1
        inorder(tree[root][1], level + 1)

if __name__ == '__main__':
    n = int(input())
    tree = {}
    row = [[] for i in range(n + 1)]
    location = 1
    for i in range(n):
        root, left, right = map(int,input().split())
        tree[root] = [left, right]
        
    # for v in tree.values(): # 최초의 코드
    #     node.extend(v)      # 딕셔너리에 대해 잘 몰라서 values 값을 node에 extend 치고
    # node = set(node)        # set으로 중복제거
    # for k in range(1,n + 1):# 이렇게 되면 for 문을 2번 돌리는 것이랑 똑같아서 비효율적임
    #     if k not in node:
    #         root = k
    #for i in range(1, n + 1):
    
    node = list(tree.values()) #values를 리스트 변환 후 1차원 리스트화 + set으로 중복제거
    node = set(list(itertools.chain(*node)))
    for i in range(1, n + 1):
        if i not in node:
            rt = i
                 
    inorder(rt, 1)
    
    dist = max(row[1]) - min(row[1]) + 1
    level = 1
    for i in range(2, n + 1):
        if row[i]:
            if dist < max(row[i]) - min(row[i]) + 1:
                dist = max(row[i]) - min(row[i]) + 1
                level = i
    print(level, dist)
    
'''
노드의 개수를 나타내는 정수 N(1 ≤ N ≤ 10,000)
n개 줄 root , left, right ( 1 ~ n)
자식이 없는 경우에는 자식 노드의 번호에 -1

예제 입력 1 
19
1 2 3
2 4 5
3 6 7
4 8 -1
5 9 10
6 11 12
7 13 -1
8 -1 -1
9 14 15
10 -1 -1
11 16 -1
12 -1 -1
13 17 -1
14 -1 -1
15 18 -1
16 -1 -1
17 -1 19
18 -1 -1
19 -1 -1
예제 출력 1 
3 18
'''