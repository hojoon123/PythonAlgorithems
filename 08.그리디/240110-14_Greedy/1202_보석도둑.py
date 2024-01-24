from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(items, bags):
    ans = 0
    tmp = []
    for bag in bags:
        while items and bag >= items[0][0]:
            heapq.heappush(tmp, -items[0][1])
            heapq.heappop(items)
        if tmp:
            ans -= heapq.heappop(tmp)
            
    return ans
def main():
    n, k = map(int,input().split())
    items = []
    for i in range(n):
        m, v = map(int,input().split())
        heapq.heappush(items, (m, v))
    bags = sorted(int(input()) for i in range(k))
    print(solve(items, bags))
    
if __name__ == "__main__":
    main()

# 가방 무게 고려해서 작은 순부터 채워야 됨.
# 가성비 고려해서 작은 거 부터 가성비 순으로 넣으면 될 듯?