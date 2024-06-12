import sys
input = sys.stdin.readline

def check(d):
    pass
            
def main():
    for _ in range(int(input())):
        n = int(input())
        d = dict()
        for num in list(map(int,input().split())):
            d[num] = 1
                
        m = int(input())
        for num in list(map(int,input().split())):
            if num in d:
                print(1)
            else:
                print(0)
    
if __name__ == "__main__":
    main()