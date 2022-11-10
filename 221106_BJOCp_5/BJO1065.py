a = int(input())
count = 0
for i in range(1,a+1):
    if i <100:
        count+=1
    else:
        b = list(map(int,str(i)))
        if((b[0]-b[1] == b[1]-b[2])):
            count+=1
print(count)
'''
첫째 줄에 1,000보다 작거나 같은 자연수 N
110
1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력
99
'''