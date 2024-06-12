import sys
input = sys.stdin.readline

def check(arr, check_list):
    ans = 0
    for i in check_list:
        if i in arr:
            ans += 1
    return ans

def main():
    n = int(input())
    entered = dict()
    for i in range(n):
        name, log = map(str,input().rstrip().split())
        if name in entered:
            del entered[name]
        else:
            entered[name] = 1
    ans = []
    for i in entered:
        ans.append(i)
    ans.sort(reverse=True)
    for i in ans:
        print(i)
if __name__ == "__main__":
    main()