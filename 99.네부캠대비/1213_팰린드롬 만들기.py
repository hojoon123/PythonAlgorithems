import sys
from collections import Counter
input = sys.stdin.readline

def magic(word_list, word_count):
    ans = ''
    cnt = 0
    middle_node = ''
    for word in word_count:
        if word_count[word] % 2 == 1:
            cnt += 1
            middle_node = word
        if cnt > 1:
            return "I'm Sorry Hansoo"
    
    for i in range(0, len(word_list), 2):
        if word_count[word_list[i]] % 2 == 1:
            word_count[word_list[i]] -= 1
        else:
            ans += word_list[i]
    
    tmp = ans[::-1]
    ans += middle_node
    ans += tmp
    return ans
        
def main():
    word_list = sorted(input().rstrip())
    word_count = Counter(word_list)
    
    print(magic(word_list, word_count))
    
    
if __name__ == "__main__":
    main()
    