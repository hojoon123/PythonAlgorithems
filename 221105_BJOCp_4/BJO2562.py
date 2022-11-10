a =[]
[a.append(int(input())) for i in range(9)]
print("%d\n%d" %(max(a),a.index(max(a))+1))