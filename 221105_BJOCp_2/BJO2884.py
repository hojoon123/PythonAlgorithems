a = list(map(int, input().split()))

if(a[1] >= 45):
    a[1]-=45
    print("%d %d" % (a[0],a[1]))
else:
    if(a[0] == 0):
        a[0]=23
    else:
        a[0]-=1
    a[1]+=15
    print("%d %d" % (a[0],a[1]))