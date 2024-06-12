import sys
input = sys.stdin.readline

def check(d):
    pass
            
def main():
    n, m = map(int,input().split())
    d = dict()
    for i in list(map(int,input().split())):
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    item = d.items()
    item = list(item)
    item.sort(key=lambda x:-x[1])
    for key, value in item:
        for j in range(d[key]):
            print(key,end=" ")
            
if __name__ == "__main__":
    main()