import sys

n = int(input())
a = []
for i in range(n):
    b = str(input())
    a.append(b)
a = list(set(a))
a.sort(key=lambda x: (len(x),x))
for i in range(len(a)):
    print(a[i])


'''
길이가 짧은 것부터
길이가 같으면 사전 순으로
 단, 같은 단어가 여러 번 입력된 경우에는 한 번씩만 출력
예제 입력 1 
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours
예제 출력 1 
i
im
it
no
but
more
wait
wont
yours
cannot
hesitate
'''