import sys
input = sys.stdin.readline

def check(n):
    d = dict()
    for _ in range(n):
        title = input().rstrip()
        if title in d:
            d[title] += 1
        else:
            d[title] = 1
    
    max_cnt = max(d.values())
    tmp = []
    for i in d:
        if d[i] == max_cnt:
            tmp.append(i)
    tmp.sort()
    return tmp[0]
            

def main():
    n = int(input())
    print(check(n))
    
if __name__ == "__main__":
    main()