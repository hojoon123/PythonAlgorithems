def check(s, t):
    q, Q, r, c = False, False, False, False
    if t < 12:
        return 'invalid'
    else:
        for e in s:
            if e.isupper():
                Q = True
            elif e.islower():
                q = True
            elif e in "+_)(*&^%$#@!./,;{}":
                r = True
            elif e.isdigit():
                c = True
    if q and Q and r and c:
        return 'valid'
    else:
        return 'invalid'

n = int(input())
for i in range(n):
    t = int(input())
    s = str(input())
    print(check(s, t))