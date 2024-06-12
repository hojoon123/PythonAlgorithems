import sys
input = sys.stdin.readline

def check(arr, check_list):
    ans = 0
    for i in check_list:
        if i in arr:
            ans += 1
    return ans

def main():
    for _ in range(int(input())):
        n = int(input())
        d = dict()
        for i in range(n):
            a, b = map(str,input().rstrip().split())
            if b in d:
                d[b] += 1
            else:
                d[b] = 1
        
        ans = 1
        for i in d:
            ans *= (d[i] + 1)
        print(ans - 1)
if __name__ == "__main__":
    main()