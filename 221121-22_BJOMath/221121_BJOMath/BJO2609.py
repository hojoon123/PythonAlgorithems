import sys
input = sys.stdin.readline

n = list(map(int,input().split()))
ans = 0; ans2 = 0
for i in range(1,max(n)+1):
    if n[0] % i or n[1] % i: # cnt로 나눴을 때 둘 다 나눠지면
        pass
    else:
        ans = i
        ans2 =(n[0] // i) * (n[1] // i) * i
print(ans)
print(ans2)


'''
예제 입력 1 
24 18
예제 출력 1 
6
72
'''