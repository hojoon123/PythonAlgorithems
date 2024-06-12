import sys
input = sys.stdin.readline

def hash(arr):
    d = dict()
    for i in arr:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def main():
    n = int(input())
    all_nums = hash(list(map(int,input().split())))
    m = int(input())
    ans = []
    for i in list(map(int,input().split())):
        if i in all_nums:
            ans.append(all_nums[i])
        else:
            ans.append(0)
    print(*ans)
    
    
if __name__ == "__main__":
    main()
    