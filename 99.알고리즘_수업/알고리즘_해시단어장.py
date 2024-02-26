import sys
import time
input = sys.stdin.readline


def create_hash_table(size):
    return [[] for _ in range(size)]

def _hash(key, size):
    return hash(key) % size

def insert(hash_table, key, value):
    hash_value = _hash(key, len(hash_table))
    for pair in hash_table[hash_value]:
        if pair[0] == key:
            pair[1] = value  # 이미 존재하는 키라면 값을 업데이트하고 종료
            return
    hash_table[hash_value].append((key, value))

def search(hash_table, key):
    hash_value = _hash(key, len(hash_table))
    for pair in hash_table[hash_value]:
        if pair[0] == key:
            return pair[1]  # 키에 해당하는 값 반환
    return None  # 키를 찾지 못한 경우 None 반환

def delete(hash_table, key):
    hash_value = _hash(key, len(hash_table))
    for i, pair in enumerate(hash_table[hash_value]):
        if pair[0] == key:
            del hash_table[hash_value][i]  # 키에 해당하는 항목 삭제
            return
    raise KeyError(f"Key '{key}' not found")

# 예시 사용
word_dict = create_hash_table(size=10)

# 단어 추가
insert(word_dict, "apple", "사과")
insert(word_dict, "banana", "바나나")
insert(word_dict, "cherry", "체리")

# 단어 검색
print(search(word_dict, "apple"))  # 출력: 사과
print(search(word_dict, "banana"))  # 출력: 바나나
print(search(word_dict, "orange"))  # 출력: None (찾을 수 없음)

# 단어 삭제
delete(word_dict, "banana")
print(search(word_dict, "banana"))  # 출력: None (삭제됨)
