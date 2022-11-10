a = int(input())
for i in range(a):
    b = list(map(str,input().split()))
    c = list(b[1])
    for j in c:
        for k in range(int(b[0])):
            print(j, end = "")
    print(" ")

'''
2
3 ABC
5 /HTP
출
AAABBBCCC
/////HHHHHTTTTTPPPPP
0부터 순차
'''