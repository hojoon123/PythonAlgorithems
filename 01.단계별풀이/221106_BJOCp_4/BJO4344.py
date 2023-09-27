import sys

a = int(input())
avr = 0
for i in range(a):
    b = list(map(int,sys.stdin.readline().split()))
    del b[0]
    count = 0
    avr = sum(b)/len(b)
    for j in range(len(b)):
        if(b[j] > avr):
            count+=1
    print("{0:0.3f}%".format(count / len(b)*100))



'''
첫째 줄에는 테스트 케이스의 개수 C
첫 수 학생의 수 N  이어서 N명의 점수
5
5 50 50 70 80 100
평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리 "%0.3f"
40.000%
'''