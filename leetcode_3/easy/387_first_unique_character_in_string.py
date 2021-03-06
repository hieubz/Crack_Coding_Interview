from collections import Counter


# class Solution:
def firstUniqChar(s: str) -> int:
    count = Counter(s)

    for i, character in enumerate(s):
        if count[character] == 1:
            return i

    return -1


s = "lleetcode"
print(firstUniqChar(s))