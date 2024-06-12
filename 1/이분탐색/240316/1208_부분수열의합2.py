import sys
from bisect import bisect_left, bisect_right, bisect
from itertools import combinations
input = sys.stdin.readline

def find_to_binary_serach(graph, target):
    return bisect_right(graph, target) - bisect_left(graph, target)

def get_sum_partial_arr(graph):
    sum_arr = []
    for i in range(1, len(graph) + 1):
        for parital_arr in combinations(graph, i):
            sum_arr.append(sum(parital_arr))
    sum_arr.sort()
    
    return sum_arr
            
def main():
    n, s = map(int,input().split())
    graph = list(map(int,input().split()))
    ans = 0

    left, right = graph[:n//2], graph[n//2:]
    left_sum, right_sum = get_sum_partial_arr(left), get_sum_partial_arr(right)
    
    for i in left_sum:
        target = s - i
        ans += find_to_binary_serach(right_sum, target)
        
    ans += find_to_binary_serach(left_sum, s)
    ans += find_to_binary_serach(right_sum, s)
    
    print(ans)
            
if __name__ =="__main__":
    main()