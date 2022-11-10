a = int(input())
b = input()
sum = 0
for i in range(3):
    print(a * int(b[2-i]))
    if(i == 2):
        print(a *int(b))