a = set(range(1,10000))
removeNum = set()
for i in range(1,10001):
    for j in str(i):
        i+= int(j)
    removeNum.add(i)
result = a - removeNum

for i in sorted(result):
    print(i)
# 다 구해놓고 if 문 없이 바로 출력해서 훨씬 빠름 이게 더 실용적
        

''' 
빠름
'''