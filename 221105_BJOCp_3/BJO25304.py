a = int(input())
b = int(input())
totalPrice = 0
for i in range(b):
    c =list(map(int,input().split()))
    totalPrice+= (c[0]*c[1])
if(a == totalPrice):
    print("Yes")
else:
    print("No")