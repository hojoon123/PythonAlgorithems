from collections import deque
import sys
import heapq
input = sys.stdin.readline

def solve(a,b,c):
    ans = []
    ans.append(int(a)+int(b)-c)
    ans.append(int(a+b)-c)
    return ans
    
def main():
    a = str(input().rstrip())
    b = str(input().rstrip())
    c = int(input())
    ans = solve(a,b,c)
    print(ans[0])
    print(ans[1])
    
    
if __name__ == "__main__":
    main()
