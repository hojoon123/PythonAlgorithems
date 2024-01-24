import sys
import heapq
input = sys.stdin.readline

def solve(tasks, md):
    tmp = [0 for _ in range(md+1)]
    
    while tasks:
        w, d = heapq.heappop(tasks)
        for i in range(d, 0, -1):
            if tmp[i] == 0:
                tmp[i] = -w
                break
    ans = sum(tmp)
    
    return ans
    
def main():
    n = int(input())
    tasks = []
    md = 0
    
    for i in range(n):
        d, w = map(int,input().split())
        heapq.heappush(tasks, (-w, d))
        if d > md:
            md =  d
            
    print(solve(tasks, md))
    
if __name__ == "__main__":
    main()
