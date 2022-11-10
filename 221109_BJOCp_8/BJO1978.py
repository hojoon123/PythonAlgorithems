a = int(input())
b = list(map(int,input().split()))
result = 0
for i in b:
    c = 0
    if i > 1:
        for j in range(2,i): #i-1 임
            if i % j ==0:
                c+=1
                break
        if(c == 0):
            result+=1
print(result)

'''

n이 되는 경우가 n을 포함해야 소수

주어진 수에서 소수의 개수 출력
예제 입력 1 
4
1 3 5 7
예제 출력 1 
3

'''