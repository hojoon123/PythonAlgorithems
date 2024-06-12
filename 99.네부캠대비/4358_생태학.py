import sys
input = sys.stdin.readline

def check(d):
    pass
            
def main():
    d = dict()
    cnt = 0
    while 1:
        unit = input().rstrip()
        if unit =="":
            break
        cnt += 1
        if unit in d:
            d[unit] += 1
        else:
            d[unit] = 1         
               
    zong = sorted(d.keys())
    for i in zong:
        print(f'{i} {(d[i] / cnt * 100):.4f}')
            
if __name__ == "__main__":
    main()