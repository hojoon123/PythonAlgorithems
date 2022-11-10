a = list(map(int,input().split()))
if(a[2] <= a[1]):
    print("-1")
    exit()

print(int(a[0]/(a[2]-a[1])+1))


'''
a[0]/a[2]-a[1]
(a[2]-a[1] * n > a[0])
print(n)
고정 제조가 판매가
예제 입력 1 
1000 70 170
예제 출력 1 
11
손익분기점

'''