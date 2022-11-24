n = int(input())#상향식코드
d = [0] * (n + 1) 
for i in range(2, n + 1):
    d[i] = d[i - 1] + 1
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)	
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
print(d[n])

'''
첫째 줄에 1보다 크거나 같고, 10^6보다 작거나 같은 정수 N 
첫째 줄에 연산을 하는 횟수의 최솟값을 출력
예제 입력 1 
2
10
예제 출력 1 
1
3
'''