from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(n,k,m,nq,mq):
    ans = 0
    socket, dist = k, 0
    for i in range(k-1):
        item = heapq.heappop(mq)
        if dist > item:
            break
    while nq:
        socket, dist = heapq.heappop(nq)
        for i in range(socket-1):
            item = heapq.heappop(mq)
            if dist > item:
                break
            
            
    if mq and dist > heapq.heappop(mq):
        ans += 1
    return ans     
def main():
    n, k, m = map(int,input().split())
    ns = list(map(int,input().split()))
    nq = []
    for item in ns:
        if item != 1:
            heapq.heappush(nq, (-item, 1))
            
    ms = list(map(int,input().split()))
    mq = []
    for item in ms:
        heapq.heappush(mq,(item))
        
    print(solve(n,k,m,nq,mq))
    
        
    
    
    
if __name__ == "__main__":
    main()
