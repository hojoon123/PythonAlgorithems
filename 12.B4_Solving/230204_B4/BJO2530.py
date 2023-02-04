h, m, s = map(int,input().split())
tmp = int(input())

s1 = (s + tmp) % 60
es = (s + tmp) // 60

m1 = (m + es) % 60
em = (m + es) // 60

h1 = (h + em) % 24

print(h1, m1, s1)