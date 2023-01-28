from sys import stdin
input = stdin.readline

def check(n):
    for i in range(n):
        print(' @@@   @@@ ')
        print('@   @ @   @')
        print('@    @    @')
        print('@         @')
        print(' @       @ ')
        print('  @     @  ')
        print('   @   @   ')
        print('    @ @    ')
        print('     @     ')
        
    
if __name__ == '__main__':
    n = int(input())
    check(n)
        
    

'''
 @@@   @@@ 
@   @ @   @
@    @    @
@         @
 @       @ 
  @     @  
   @   @   
    @ @    
     @   
'''