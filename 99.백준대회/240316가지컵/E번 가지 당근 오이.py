import sys
from collections import Counter
input = sys.stdin.readline

def solve(gs, ds, os, ns, n, s, role, vegetables):
    if vegetables.count(1) == 3:
        print("비김 말하는 모든 것 가능")
        
    
def main():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        s = str(input().rstrip())
        role = str(input().rstrip())
        table = set([(s[i], role[i]) for i in range(n)])
        gs, ds, os, ns = dict(), dict(), dict(), dict()
        vegetables = [0,0,0] # G D O
        for tmp in table:
            if tmp[0] == "G":
                gs.append(tmp[1])
                vegetables[0] = 1
            elif tmp[0] == "D":
                ds.append(tmp[1])
                vegetables[1] = 1
            elif tmp[0] == "O":
                os.append(tmp[1])
                vegetables[2] = 1
            else:
                ns.append(tmp[1])
        result = []
        print(table)
        print(gs, ds, os, ns)
        solve(gs, ds, os, ns, n, s, role, vegetables)
        
    
    
if __name__ == "__main__":
    main()
