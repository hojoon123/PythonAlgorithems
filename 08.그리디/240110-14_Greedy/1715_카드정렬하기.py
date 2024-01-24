from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(li):
    ans = 0
    while li:
        tmp = 0
        for i in range(2):
            if li:
                tmp += heapq.heappop(li)
        
        ans += tmp
        if li:
            heapq.heappush(li, tmp)

    return ans

def main():
    n = int(input())
    heap_list = []
    for i in range(n):
        heapq.heappush(heap_list, int(input()))
    if n == 1:
        print(0)
        return
    print(solve(heap_list))
    
if __name__ == "__main__":
    main()
