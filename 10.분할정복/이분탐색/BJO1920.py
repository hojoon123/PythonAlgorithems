import sys
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline

def check(board, target_list):
    board.sort()
    for target in target_list:
        idx = bisect_left(board, target)
        if idx < len(board) and board[idx] == target:
            print(1)
        else:
            print(0)
            
if __name__ =="__main__":
    n = int(input())
    board = list(map(int,input().split()))
    m = int(input())
    target_list = list(map(int,input().split()))
    check(board, target_list)
    


'''
예제 입력 1 
5
4 1 5 2 3
5
1 3 7 9 5
예제 출력 1 
1
1
0
0
1
'''