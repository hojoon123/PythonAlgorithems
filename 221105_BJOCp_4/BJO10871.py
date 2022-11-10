n, x = map(int,input().split())
a = list(map(int,input().split()))

for i in range(n):
    if(x > a[i]):
        print(a[i], end = " ")

'''
예제 입력 1 
10 5
1 10 4 9 2 3 8 5 7 6
예제 출력 1 
1 4 2 3'''