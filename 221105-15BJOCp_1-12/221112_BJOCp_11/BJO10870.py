def fac(n):
    if(n <= 1):
        return n
    else:
        return fac(n-1) + fac(n-2)

a = int(input())
print(fac(a))

'''

예제 입력 1 
10
예제 출력 1 
55
'''