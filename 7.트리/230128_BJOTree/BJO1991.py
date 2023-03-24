from sys import stdin
from collections import deque
input = stdin.readline


def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right
 
 
def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root
        
# 레벨 순회
def levelorder(root):
    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        if node != '.':
            print(node, end='')
            if tree[node][0]:   
                q.append(tree[node][0])
            if tree[node][1]:
                q.append(tree[node][1])

if __name__ == '__main__':
    n = int(input())
    tree = {}
    for i in range(n):
        root, left, right = map(str,input().split())
        tree[root] = [left, right]
    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')
    print()
    
    
'''
노드의 이름은 A부터 차례대로 알파벳 대문자로 매겨지며, 항상 A가 루트 노드
예제 입력 1 
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
예제 출력 1 
ABDCEFG
DBAECFG
DBEGFCA
'''