from math import gcd

for _ in range(int(input())):
    n = list(map(int,input().split()))
    ans = 0
    for i in range(1,n[0]+1):
        for j in range(i+1, n[0]+1):
            ans += gcd(n[i],n[j])
    print(ans)

        

'''
예제 입력 1 
3
4 10 20 30 40
3 7 5 12
3 125 15 25
예제 출력 1 
70
3
35
'''