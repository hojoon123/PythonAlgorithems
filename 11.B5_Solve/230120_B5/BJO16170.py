from sys import stdin
from datetime import datetime as dt
input = stdin.readline

def check():
    format_data = "%Y\n%m\n%d"
    d = dt.now().strftime(format_data)
    print(d)

if __name__ == '__main__':
    check()
        
    
    
'''
2018
09
29
2015-01-24
'''