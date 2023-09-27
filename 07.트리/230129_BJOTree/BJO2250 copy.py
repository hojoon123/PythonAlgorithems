import sys
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
    tree = [[] for i in range(n + 1)]
    node = [0] * (n + 1)
    row = [[] for i in range(n + 1)]
    location = 1
    for i in range(n):
        root, left, right = map(int,input().split())
        tree[root].append(left)
        tree[root].append(right)
        node[root] += 1
        if left != -1:
            node[left] += 1
        if right != -1:
            node[right] += 1
    
    for i in range(1, n + 1):
        if node[i] == 1:
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