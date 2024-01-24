import sys
input = sys.stdin.readline

def solve(nums, n, k):
    stack = []
    for num in nums:
        while stack and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k > 0:
        return stack[:-k]
    else:
        return stack

def main():
    n, k = map(int,input().split())
    nums = input().rstrip()
    print(*solve(nums, n, k),sep="")
    
if __name__ == "__main__":
    main()
