import sys
input = sys.stdin.readline

def check(arr, check_list):
    ans = 0
    for i in check_list:
        if i in arr:
            ans += 1
    return ans

def main():
    n, m = map(int,input().split())
    s = dict()
    for i in range(n):
        tmp = input().rstrip()
        if tmp in s:
            continue
        else:
            s[tmp] = 1
    check_list = [input().rstrip() for i in range(m)]
    print(check(s, check_list))
    
if __name__ == "__main__":
    main()