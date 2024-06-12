import sys
from collections import deque
input = sys.stdin.readline

def check(n, d, d_list):
    ans = 0
    cnt = 0
    for i in range(n):
        s = input().rstrip()
        if s == d_list[0]:
            ans += cnt
            cnt = 0
            d[s] = 0
            d_list.popleft()
            if i == (n-1):
                break
            while not d[d_list[0]]:
                d_list.popleft()
                if not d_list:
                    return ans
        elif d[s] == 1:
            cnt += 1
            d[s] = 0

    return ans
    
            
def main():
    n = int(input())
    d = dict()
    d_list = deque()
    for i in range(n):
        s = input().rstrip()
        d_list.append(s)
        d[s] = 1
    print(check(n, d, d_list))
            
if __name__ == "__main__":
    main()