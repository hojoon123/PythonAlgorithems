t = int(input())
for i in range(t):
    a = int(input())#층
    b = int(input())#호수
    result = [i for i in range(1,b+1)] # 0층 사람
    
    for i in range(a): # 층 마다 반복하기
        for j in range(1,b): #이전 호수의 사람 데리고 살기
            result[j] += result[j-1]
    print(result[-1])

'''
t , k , n
 t 마다 집에 거주민 수를 출력
 a층의 b호에 살려면 자신의 아래(a-1)층의 1호부터 b호까지 사람들의 수의 합만큼 사람들을 데려와
 (a-1) 1~b 
 0층부터 있고 각층에는 1호부터 있으며, 0층의 i호에는 i명 1 1 2 2 3 3
 for i in range 
  k층에 n호에는 몇 명이 살고 있는지 출력

예제 입력 1 
2
1
3
2
3
예제 출력 1 
6
10
'''