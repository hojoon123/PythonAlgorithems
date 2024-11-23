def self_input():
    t = int(input())
    for i in range(1, t+1):
        n, d, x = map(int,input().split())
        boxes = list(map(int,input().split()))
        res = main(n,d,x,boxes)
        print(f"#{i} {res}")
        
def main(n,d,x,boxes):
    cnt = boxes[d-1] * n

    if x-1 > d-1:
        cnt += (x-1) - (d-1)
    elif x-1 < d-1:
        cnt += (x-1) + (n-1) - (d-1)
    return cnt
    
    
    

if __name__ == "__main__":
    self_input()