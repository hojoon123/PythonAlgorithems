def fac(n):
    if(n > 1):
        return n * fac(n - 1)
    else:
        return 1

a = int(input())
print(fac(a))

'''
예제 입력 1 
10
예제 출력 1 
3628800
'''