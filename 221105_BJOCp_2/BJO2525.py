a = list(map(int, input().split()))
b = int(input())

if(a[1]+b >= 60):
    a[1]+= b
    
    a[0]+= a[1]/60
    a[1] = a[1]%60
    
    if(a[0] >= 24):
        a[0]-=24
    print("%d %d" % (a[0],a[1]))
else:
    a[1]+= b
    print("%d %d" % (a[0],a[1]))