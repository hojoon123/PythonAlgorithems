def self_input():
    t = int(input())
    for i in range(1, t+1):
        n, d, x = map(int,input().split())
        boxes = list(map(int,input().split()))
        res = main(n,d,x,boxes)
        print(f"#{i} {res}")
        
def main(n,d,x,boxes):
    cnt = 0
    while True:
        for i in range(n):
            if x-1-i == 0:
                x = n
                i = 0
            boxes[x-1-i] -= 1
            if x-1-i == d-1 and boxes[x-1-i] == -1:
                return cnt
            cnt += 1
    
    

if __name__ == "__main__":
    self_input()