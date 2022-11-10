a = int(input()) 
b = int(input())
num = [i for i in range(a,b+1)]

result = 0
for i in num:
    c = 0
    if i > 1:
        for j in range(2,i): #i-1 임
            if i % j ==0:
                c+=1
                break
        if(c == 0):
            if(result == 0):
                minNum = i
            result+= i
            
if result == 0 :
    print("-1")
else:
    print(result)
    print(minNum)
'''
a / b 입력
합 / 최소값 출력
소수가 없을 경우는 -1을 출력

예제 입력 1 
60
100
예제 출력 1 
620
61

'''