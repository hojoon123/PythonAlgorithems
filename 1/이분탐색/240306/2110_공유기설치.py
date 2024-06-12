import sys
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline

def find_max_dist(n, c, h):
    h.sort()
    s, e  = 1, h[n-1] - h[0]
    if c == 2:
        return e
    else:
        while (s < e):
            mid = (s + e) // 2
            cnt = 1
            pre_h =  h[0]
            
            for i in range(n):
                if h[i] - pre_h >= mid:
                    cnt += 1
                    pre_h = h[i]
            if cnt >= c:
                ans = mid
                s = mid + 1
            else:
                e = mid
    return ans
            
def main():
    n, c = map(int,input().split())
    graph = [int(input()) for i in range(n)]
    print(find_max_dist(n, c, graph))
            
if __name__ =="__main__":
    main()