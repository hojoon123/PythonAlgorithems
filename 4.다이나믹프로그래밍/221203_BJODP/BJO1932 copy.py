n = int(input())
t = []
k = 2
for i in range(n):
    t.append(list(map(int, input().split())))
for i in range(1, n):
    for j in range(k):
        if j == 0:
            t[i][j] = t[i][j] + t[i - 1][j]
        elif i == j:
            t[i][j] = t[i][j] + t[i - 1][j - 1]
        else:
            t[i][j] = max(t[i - 1][j - 1], t[i - 1][j]) + t[i][j]
    k += 1
print(max(t[n - 1]))
#점화식은 같으나, 훨씬 잘 했다고 생각한 코드
#불필요한 dp,tmp 리스트를 없애고 최초로 생성한 삼각형 배열에 그대로 덧씌움
#나는 이걸 못 해서 for(n) 문 내부에 for k 를 따로 두번이나 씀 되게 없어보이죠..
#푼 건 맞지만 이게 훨씬 명확한 코드다
'''
예제 입력 1 
5
7
3 8
8 1 0
2 7 4 4
4 5 2 6 5
예제 출력 1 
30
'''