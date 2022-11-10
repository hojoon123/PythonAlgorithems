def d(n):
    n = n+sum(map(int,str(n)))
    return n

a = []
for i in range(1,10001):
    a.append(d(i))

for i in range(1,10001):
    if i not in a:
        print(i)
#느림 정직하게 만번을 돌리고 if 문에 넣기 때문에 느림