import sys
input = sys.stdin.readline

def check(d):
    pass
            
def main():
    n = int(input())
    d = dict()
    d["ChongChong"] = 1
    for _ in range(n):
        a, b = map(str,input().rstrip().split())
        if (a in d) or (b in d):
            d[a], d[b] = 1, 1
    print(len(d))
            
if __name__ == "__main__":
    main()