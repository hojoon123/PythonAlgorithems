import sys
input = sys.stdin.readline

def check(d):
    pass
            
def main():
    n = int(input())
    ans = 0
    cnt = 0
    for i in range(n):
        tmp = input().rstrip()
        if tmp == "ENTER":
            d = dict()
            ans += (cnt - 1)
            cnt = 0
        if tmp in d:
            continue
        else:
            d[tmp] = 1
            cnt += 1
    ans += cnt
    print(ans)
    
if __name__ == "__main__":
    main()