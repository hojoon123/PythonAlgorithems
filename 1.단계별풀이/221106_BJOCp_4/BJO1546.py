import sys 

a = int(input())
b = list(map(int,sys.stdin.readline().split()))
result= 0
for i in range(a):
    result += b[i]/max(b)*100
print(result/len(b))

'''
최고점이 70이고, 수학점수가 50이었으면 수학점수는 50/70*100이 되어 71.43점
3
40 80 60
첫째 줄에 새로운 평균을 출력
75.0
'''