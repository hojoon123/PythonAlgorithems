N = int(input())
a = [0] * (N+1); result = 0
price = [0] + list(map(int,input().split()))
for i in range(1,N+1): a[i] = (N/(i)) * price[i] 
tmp = a.index(max(a))
result += price[tmp] * (N//tmp) 
N = N % tmp
tmp = a.index(max(a[:N+1]))
while N > 0:
    N -= tmp
    result += price[tmp]
    if tmp > N: 
        tmp = a.index(max(a[:N+1]))
print(result)

'''
그리드 방식으로 풀었음. 그러나 틀림
해당 과정에서 가성비가 높더라도 안될수가 있음
반례
5
1 9 18 25 1
답이 27이어야 하는데, 26
4번의 가성비가 가장 높음으로서 벌어지는 반례
5
1 4 5 20 24
답이 24여야 하는데 21이 나옴 20의 가성비가 더 높기에 20+1이 24보다 작음에도 불구하고 반례가 나옴
'''