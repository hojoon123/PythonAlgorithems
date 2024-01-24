import sys
import heapq
input = sys.stdin.readline

def plus_check(plus, ans, m, first):
    cnt = 0
    while plus:
        if cnt == 0:
            ans += (plus.pop() * first)
            cnt += 1
        else:
            cnt += 1
            plus.pop()
        if cnt == m:
            cnt = 0
            if first == 1:
                break
    return (plus, ans)

def minus_check(minus, ans, m, first):
    cnt = 0
    while minus:
        if cnt == 0:
            ans -= (minus.pop(0) * first)
            cnt += 1
        else:
            cnt += 1
            minus.pop(0)
        if cnt == m:
            cnt = 0
            if first == 1:
                break
    return (minus, ans)
            
def solve(m, sorted_nums):
    plus = []
    minus = []
    ans = 0
    for num in sorted_nums:
        if num > 0:
            plus.append(num)
        else:
            minus.append(num)
    
    if plus and minus:
        if plus[-1] > -minus[0]:
            plus, ans = plus_check(plus, ans, m, 1)
        else:
            minus, ans = minus_check(minus, ans, m, 1)
    else:
        if plus:
            plus, ans = plus_check(plus, ans, m, 1)
        else:
            minus, ans = minus_check(minus, ans, m, 1)
    
    plus, ans = plus_check(plus, ans, m, 2)
    minus, ans = minus_check(minus, ans, m, 2)
    
    return ans
    
def main():
    n, m = map(int,input().split())
    nums = sorted(map(int,input().split()))
    print(solve(m,nums))
    
if __name__ == "__main__":
    main()
