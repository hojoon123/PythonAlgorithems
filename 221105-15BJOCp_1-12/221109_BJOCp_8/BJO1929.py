import sys
input = sys.stdin.readline

a, b = map(int,input().split()) 

for i in range(a,b+1):
    c = 0
    if i> 1:
        for j in range(2,int(i**0.5) + 1): #i-1 까지임
            if i % j == 0:
                c+=1
                break
        if(c == 0):
            print(i)
''' 
에라토스테네스의 체 사용해야 빠름
1 ≤ M ≤ N ≤ 1,000,000
 M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다
 한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다.
예제 입력 1 
3 16
예제 출력 1 
3
5
7
11
13

'''