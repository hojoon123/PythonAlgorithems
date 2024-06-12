import sys
input = sys.stdin.readline

def check(s,ls):
    d = dict()
    for i in range(ls):
        for j in range(i, ls):
            if s[i:j+1] in d:
                continue
            else:
                d[s[i:j+1]] = 1
    
    ans = len(d)
    return ans

def main():
    s = input().rstrip()
    ls = len(s)
    print(check(s, ls))
    
    
if __name__ == "__main__":
    main()