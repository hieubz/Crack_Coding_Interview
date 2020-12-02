# find the first non-repeating character in it and return its index
# can use Counter to accelerate
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts = {}
        for c in s:
            dicts[c] = dicts.get(c, 0) + 1

        for i, ch in enumerate(s):
            if dicts[ch] == 1:
                return i
        return -1
