n = int(input())
s = ''
if n == 0:
    print(0)
while n != 0:
    if n % -2:
        n = n//-2 + 1
        s = '1'+ s
    else:
        n = n//-2
        s = '0' + s
print(s)
#n = (n // a) + (n % a) 이렇게 해도 되긴하는데, 그러면 연산을 두번 함 이걸 반틈으로 줄이기
#위해서 어차피 짝수니까 1가지로 나눔


'''
-2,000,000,000 ≤ N ≤ 2,000,000,000
-2진법 수를 출력
예제 입력 1 
-13
예제 출력 1 
110111
'''