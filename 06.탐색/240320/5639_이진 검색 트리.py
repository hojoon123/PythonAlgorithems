import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def preorder_to_postorder(preorder):
    if len(preorder) == 0:
        return
    
    left, right = [], []
    v = preorder[0]
    
    for i in range(1, len(preorder)):
        if preorder[i] > v:
            left = preorder[1:i]
            right = preorder[i:]
            break
    else:
        left = preorder[1:]

    preorder_to_postorder(left)
    preorder_to_postorder(right)
    print(v)
    
if __name__ == '__main__':
    preorder = []
    while True:
        try:
            node = int(input())
            preorder.append(node)
        except:
            break
        
    preorder_to_postorder(preorder)