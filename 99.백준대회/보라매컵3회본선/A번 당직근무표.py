import sys
from collections import Counter
input = sys.stdin.readline

def solve(n,arr):
    ns = list(set(arr))
    mn = Counter(arr).most_common(1)[0][1]
    if (mn - 1) > (n - mn):
        return "NO"
    else:
        return "YES"
    
def main():
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr))
    
    
if __name__ == "__main__":
    main()
