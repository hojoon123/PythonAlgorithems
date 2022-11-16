x = int(input())
for i in range(x):
    a = list(map(int,input().split()))
    n = 1
    while 1:
        if(a[2]-a[0]*n > 0):
            n+=1
        else:
            print((a[2]-a[0]*(n-1))*100+n)
            break
'''
n = 1
10 - 6n 
if(a[2] - a[0]*n > 0):
    n+=1
else:
    층수 = a[2]-a[0]*n
n = 호수
a[0] = 층 a[1] = 방 a[2] = 손놈번호
예제 입력 1 
2
6 12 10
30 50 72
예제 출력 1 
402
1203

'''