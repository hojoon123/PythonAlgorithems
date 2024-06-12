import sys
from bisect import bisect_left, bisect_right, bisect
input = sys.stdin.readline

def get_similar_zero(n, graph):
    ans = int(1e11)
    
    for i in range(n-2):
        left = i + 1
        right = n - 1
        while left < right:
            tmp = graph[left] + graph[right] + graph[i]

            if ans > abs(tmp):
                ans = abs(tmp)
                start, end, mid = graph[left], graph[right], graph[i]
                if tmp == 0:
                    break
                
            if tmp < 0:
                left += 1
            else:
                right -= 1
        
    return start, mid, end
        
            
def main():
    n = int(input())
    graph = sorted(map(int,input().split()))
    print(*sorted(get_similar_zero(n,graph)))
            
if __name__ =="__main__":
    main()