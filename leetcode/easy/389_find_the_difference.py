class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dicts = {}
        for c in s:
            dicts[c] = dicts.get(c, 0) + 1

        for c in t:
            if dicts.get(c, 0) == 0:
                return c
            else:
                dicts[c] -= 1

    def findTheDifference_2(self, s, t):
        diff = 0
        for i in range(len(s)):
            diff -= ord(s[i])
            diff += ord(t[i])

        diff += ord(t[-1])

        return chr(diff)

    def findTheDifference_3(self, s, t):
        code = 0
        for c in s + t:
            code ^= ord(c)

        return chr(code)
