a = int(input())
count = 0
fN = a
cal = 0
while 1:
    cal = a//10 + a%10
    a = a%10 * 10 + cal%10
    count+=1
    if(fN == a):
        print("%d" %count)
        break