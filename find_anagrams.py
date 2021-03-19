from collections import Counter
from typing import List

def find_anagrams(s: str, p:str) -> List[int]:
    p_counter = Counter(p)
    result = []
    i = 0
    while i + len(p) < len(s):
        if Counter[s[i:i+len(p)]] == p_counter:
            result.append(i)
    return result
