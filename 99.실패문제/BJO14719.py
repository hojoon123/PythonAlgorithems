a, b = map(int,input().split())
x = list(map(int,input().split()))
mn = x.index(max(x)) #x의 최고값의 index
result = 0

if max(x[0 : mn]) != x[0]: # 왼쪽 끝이 최고값이 아닐 때
    
    if x[0 : mn].count(max(x[0 : mn])) > 1: #사이의 값 중에 최고값이 
        while x[0 : mn].count(max(x[0 : mn])) == 1:
            x.remove(max(x[0 : mn]))
            break
        pass
        # 1 0 3 1 2 3 4 1 1 2
        # 1 0 3 1 2 4 4 4 1 1 2
        # 먼저 최고값이 1이 될 때까지 깍고 시작하기
        # mn 부터 현재 최고값 사이에서 집어넣고 
        # 1 0 1 1 2 3 4 1 1 2
    else:
        pass
else: # 왼쪽 끝이 최고값일 때
    for i in x[0 : mn]:
        result += x[0] - i
        

if max(x[mn+1 : len(x)]) != x[-1] :
    pass
else: # 오른 쪽 끝이 최고값일 때
    for i in x[mn+1 : len(x)]:
        result += x[-1] - i
print(result)
    
'''
x[0 : rr-1]
x[0] ~ x[rr-1] max 값이 == x[0] 아니면 반복 
제일 양쪽 끝에 가까운 최고값으로 선택하면 되잖아 그렇게 되게 하면 되잖아
index(max())로 하면 앞에꺼부터 나옴 뒤에꺼 마려우면?
max()의 a.count(max()) 가 1 이상이면 a.count(max())-1 만큼 max()지우기

1 0 3 1 2 3 4 1 1 2
제일 큰 수 기준으로 가르고 
제일 양쪽 수가 큰 수 기준으로 가장 큰 값이
아닐 경우 사이에서 가장 큰 값a 찾고 a 기준으로 자리마다 a-자리 sum 에다가 넣기 
또 a 기준으로 다시 양쪽 수가 가장 큰 값인지 보고
양쪽 수가 가장 큰 값이면 멈추기
예제 입력 1 
4 4
3 0 1 4
4 8
3 1 2 3 4 1 1 2
1 0 3 1 2 3 4 1 1 2
예제 출력 1 
5  
5
'''