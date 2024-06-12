import sys
input = sys.stdin.readline

def check(d):
    arr = []
    for key, value in d.items():
        arr.append((key,value,len(key)))
    arr.sort(key=lambda x: (-x[1], -x[2], x[0]))
    return arr
            

def main():
    n, m = map(int,input().split())
    d = dict()
    for i in range(n):
        word = input().rstrip()
        if len(word) >= m:
            if word in d:
                d[word] += 1
            else:
                d[word] = 1
                
    ans = check(d)
    for i in ans:
        print(i[0])
    
if __name__ == "__main__":
    main()