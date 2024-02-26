a = list(map(int, input().split()))
stack = 1
for i in range(3):
    if(a.count(a[i]) > stack):
        stack = a.count(a[i])
        num = a[i]
if stack == 3: dividend = 10000 + (num * 1000)
elif stack == 2: dividend = 1000 + (num * 100)
else: dividend = max(a) * 100

print(dividend)