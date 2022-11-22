from math import sqrt
#혼자서 너무 심심하고 힘들어서 재밌게 해보고자 낙서 좀 했습니다...
pnum = []; arr = [1]*1000001 # 1000000이하의 소수를 미리 다 구해놓음 pnum에
for i in range(2, 1000001): #난 왜 이런 생각이 바로바로 안 나오는걸까...
    if arr[i] == 1:
        pnum.append(i)
        for j in range(2*i, 1000001, i):
            arr[j] = 0
arr[0], arr[1] = 0, 0 #b - i가 만약 20이면 20 - 19 arr[1] 이거 때문에 cnt가 1개 추가될 수 있음. 

for _ in range(int(input())):
    b = int(input())
    cnt = 0
    for i in pnum:
        if i >= b:
            break
        if arr[b-i] and i <= b-i: # b-i가 소수니? 그리고 소수 i 는 b-i 보다 작니?(중복방지)
            cnt += 1 #20기준 2, 3 ,5, 7, 11, 13, 17, 19 arr[18],arr[17],arr[15],arr[9],arr[7],arr[1]
    print(cnt) #만약 arr[b-1]이 소수라면 i도 소수니까 더했을 때 값이 나옴 고로 cnt+=1
                #와 진짜 세상에 왜 이렇게 똑똑한 사람이 많을까..
'''
예제 입력 1 
5
6
8
10
12
100
예제 출력 1 
1
1
2
1
6
'''