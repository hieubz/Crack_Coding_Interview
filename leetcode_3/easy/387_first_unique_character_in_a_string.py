from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = Counter(s)
        for i, c in enumerate(list(s)):
            if count[c] == 1:
                return i

        return -1