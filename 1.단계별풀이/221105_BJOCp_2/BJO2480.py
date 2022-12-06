a = list(map(int, input().split()))
stack = 1
for i in range(3):
    if(a.count(a[i]) > stack):
        stack = a.count(a[i])
        num = a[i]
if stack == 3: dividend = 10000 + (num * 1000)
elif stack == 2: dividend = 1000 + (num * 100)
else: dividend = max(a) * 100

print(dividend)

'''
예제 입력 1 
3 3 6
예제 출력 1 
1300

같은 눈이 3개가 나오면 10,000원+(같은 눈)×1,000원의 상금을 받게 된다. 
같은 눈이 2개만 나오는 경우에는 1,000원+(같은 눈)×100원의 상금을 받게 된다. 
모두 다른 눈이 나오는 경우에는 (그 중 가장 큰 눈)×100원의 상금을 받게 된다.  
'''