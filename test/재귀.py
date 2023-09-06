#재귀함수 사용
def basic_factorial(n):
    print(f"재귀함수 실행 현재 n은 {n}")
    if n > 1:
        return n * basic_factorial(n - 1)
    else:
        return 1

#꼬리함수 사용
def tail_factorial(n, total):
    print(f"재귀함수 실행 현재 n은 {n}")
    if n > 1:
        return tail_factorial(n - 1, total * n)
    else:
        return total

def factorial(n):
    ans = 1
    for i in range(n,0,-1):
        ans *= i
    return ans

a = int(input("팩토리얼을 구할 숫자를 입력하세요 : "))
#print(basic_factorial(a))
print(tail_factorial(a,1))
print(factorial(a))