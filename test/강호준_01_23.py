from sys import stdin
from collections import deque
input = stdin.readline

def F(target_idx):
    q = deque()
    q.append((0,0)) # [0] = idx [1] = f(idx)
    q.append((1,1))
    
    while q:
        idx, fn = q.popleft()
        if idx == target_idx:
            return fn
        q.append((idx + 2, fn + q[0][1]))
    
if __name__ == "__main__": # 메인문입니다.
    user_input = int(input())
    print(F(user_input))
'''
큐 써서 n 값을 받으면 F(n) 출력
'''    