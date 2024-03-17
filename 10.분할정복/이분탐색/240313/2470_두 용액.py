import sys
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline

def get_similar_zero(n, graph):
    left = 0
    right = n - 1
    ans = abs(graph[left] + graph[right])
    start, end = graph[left], graph[right]
    
    while left < right:
        tmp = graph[left] + graph[right]
        if ans > abs(tmp):
            ans = abs(tmp)
            start, end = graph[left], graph[right]
            if ans == 0:
                break
        if tmp < 0:
            left += 1
        else:
            right -= 1
    return start, end
        
            
def main():
    n = int(input())
    graph = sorted(map(int,input().split()))
    print(*get_similar_zero(n,graph))
            
if __name__ =="__main__":
    main()