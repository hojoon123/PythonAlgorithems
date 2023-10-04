import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# (n-1) * 3
def ps_1(n):
    res = (n - 1) * 3
    return res

# 2 ** (n + 1)
def ps_2(n):
    res = 2 ** (n + 1)
    return res

# n * (n + 1) / 2 
def ps_3(n):
    res = n * (n + 1) // 2 
    return res

# log2(n) + 1
def ps_4(n):
    res = 0
    while n >= 2:
        n /= 2
        res += 1
    res = res + 1
    return res

# int((3/2) * n)    
def ps_5(n):
    res = n
    while n >= 3:
        n /= 3
        res += n
        print(n)
    res = int(res)
    return res

# int((3/2) * n)
def ps_5anoter(n):
    res = int((3/2) * n)
    return res

if __name__ == "__main__": # 메인문입니다.
    user_input = int(input())
    print(ps_1(user_input))
    print(ps_2(user_input))
    print(ps_3(user_input))
    print(ps_4(user_input))
    print(ps_5(user_input))
    print(ps_5anoter(user_input))
'''
(1) T(n) = T(n-1) + 3 for n > 1, T(1) = 0
    (n - 1) * 3

(2) T(n) = 2T(n-1) for n > 1, T(1) = 4
    2 ** (n + 1)
    
(3) T(n) = T(n-1) + n for n > 0, T(0) = 0
    n * (n + 1) // 2 
    
(4) T(n) = T(n/2) + 1 for n > 1, T(1) = 1   (n = 2**k)
    log2(n) + 1

(5) T(n) = T(n/3) + n for n > 1, T(1) = 1   (n = 3**k)
    log3(3)부터log3(n)까지의 수를 더한 값 + n
    int((3/2) * n)
'''    