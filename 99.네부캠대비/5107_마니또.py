import sys
input = sys.stdin.readline

def check_link(start, d_list, d):
    while start not in d_list:
        d_list.add(start)
        start = d[start]
    return d_list

def main():
    case =1
    n = int(input())
    
    while n != 0:
        d =dict()
        for _ in range(n):
            manitto, target = input().strip().split()
            d[manitto] = target
            
        cnt =0
        d_list = set()
        
        for manitto in d.keys():
            if manitto not in d_list :
                d_list = check_link(manitto, d_list, d)
                cnt += 1
        print(case, cnt)
        
        case +=1
        n = int(input())

if __name__ == "__main__":
    main()