import sys

input = sys.stdin.readline

a = []
for i in range(5):
    a.append(int(input()))
a.sort()
print(int(sum(a) / 5))
print(a[2])
    

'''
첫째 줄부터 다섯 번째 줄
첫째 줄에는 평균을 출력하고, 둘째 줄에는 중앙값
예제 입력 1 
10
40
30
60
30
예제 출력 1 
34
30
'''