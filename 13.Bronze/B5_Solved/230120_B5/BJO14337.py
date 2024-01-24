from sys import stdin
input = stdin.readline

def check(n):
    print(':fan::fan::fan:')
    print(':fan::{0}::fan:'.format(n))
    print(':fan::fan::fan:')

if __name__ == '__main__':
    n = str(input().rstrip())
    check(n)
        
    
    
'''
:fan::fan::fan:
:fan::appa::fan:
:fan::fan::fan:
'''