from sys import stdin
from collections import deque
input = stdin.readline

class Node():
    def __init__(self, item):
        self.item = item
        self.left = self.right = None
        
class BinaryTree():
    def __init__(self):
        self.root = None

    #전위순회
    def preorder(self):
            def _preorder(node):
                print(node.item, end=' ')
                if node.left:
                    _preorder(node.left)
                if node.right:
                    _preorder(node.right)
            _preorder(self.root)

    #중위 순회
    def inorder(self):
        def _inorder(node):
            if node.left:
                _inorder(node.left)
            print(node.item, end=' ')
            if node.right:
                _inorder(node.right)
        _inorder(self.root)
        

    #후위 순회
    def postorder(self):
        def _postorder(node):
            if node.left:
                _postorder(node.left)
            if node.right:
                _postorder(node.right)
            print(node.item, end=' ')
        _postorder(self.root)
        

    #레벨 순회
    def levelorder(self):
        q = deque([self.root])
        while q:
            node = q.popleft()
            print(node.item, end=' ')
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
    
if __name__ == '__main__':
    BT = BinaryTree()
    N1 = Node(1)
    N2 = Node(2)
    N3 = Node(3)
    N4 = Node(4)
    N5 = Node(5)
    N6 = Node(6)
    N7 = Node(7)
    N8 = Node(8)

    BT.root = N1
    N1.left = N2
    N1.right = N3
    N2.left = N4
    N2.right = N5
    N3.left = N6
    N3.right = N7
    N4.left = N8

    print('preorder')
    BT.preorder()

    print('\ninorder')
    BT.inorder()

    print('\npostorder')
    BT.postorder()

    print('\nlevelorder')
    BT.levelorder()
    
    
'''
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