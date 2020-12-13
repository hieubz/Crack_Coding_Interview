from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:

        dicts = Counter(s)

        for i in range(len(s)):
            if dicts[s[i]] == 1:
                return i

        return -1
