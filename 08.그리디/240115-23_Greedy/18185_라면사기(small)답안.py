import sys
input = sys.stdin.readline

def buy1(factory,n, ans): # 1개 살 경우
    ans += 3 * factory[n]
    return ans

def buy2(factory,n,ans): # 2개 살 경우
    m = min(factory[n:n+2])
    factory[n] -= m
    factory[n+1] -= m
    ans += 5* m    
    return ans

def buy3(factory,n, ans): # 3개 살 경우
    m = min(factory[n:n+3])
    factory[n] -= m
    factory[n+1] -= m
    factory[n+2] -= m
    ans += 7* m
    return ans

def main():
    n = int(input())
    factory = list(map(int,input().split())) + [0,0]
    ans = 0
    for i in range(len(factory)-2):
        if factory[i+1] > factory[i+2]: # i만큼 빼면 안될때 [2, 3, 2, 1]
            m = min(factory[i], factory[i+1] - factory[i+2])
            factory[i] -= m
            factory[i+1] -= m
            ans += 5*m
            ans = buy3(factory,i,ans)
            ans = buy1(factory,i,ans)
        else :
            ans = buy3(factory,i,ans)
            ans = buy2(factory,i,ans)
            ans = buy1(factory,i,ans)
    print(ans)
    
if __name__ == "__main__":
    main()
