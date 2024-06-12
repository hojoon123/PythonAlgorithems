import sys
from itertools import combinations
input = sys.stdin.readline

def check(start, d_list, d):
    pass

def main():
    n = int(input())
    n_list = list(map(int,input().split()))
    nums = set()
    ans = sum(n_list)
    for i in range(1,n+1):
        for j in combinations(n_list,i):
            nums.add(sum(j))
    ans -= len(nums)
    print(ans)    

if __name__ == "__main__":
    main()