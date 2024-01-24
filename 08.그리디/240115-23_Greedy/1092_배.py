import sys
input = sys.stdin.readline

def solve(crains, boxes):
    cnt = 0
    if boxes[0] > crains[0]:
        return -1
    
    while boxes:
        for crain in crains:
            if boxes and crain < boxes[-1]:
                continue
            for idx in range(len(boxes)):
                if crain >= boxes[idx]:
                    boxes.pop(idx)
                    break
        cnt += 1
    return cnt

def main():
    n = int(input())
    crains = sorted(map(int,input().split()), reverse=True)
    m = int(input())
    boxes = sorted(map(int,input().split()), reverse=True)

    print(solve(crains, boxes))
    
if __name__ == "__main__":
    main()
