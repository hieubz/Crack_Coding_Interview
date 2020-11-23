# find the first non-repeating character in it and return its index
# can use Counter to accelerate
class Solution:
    def firstUniqChar(self, s: str) -> int:
        dicts = {}
        for charac in s:
            if charac not in dicts:
                dicts[charac] = 1
            else:
                dicts[charac] += 1

        for i, c in enumerate(s):
            if dicts[c] == 1:
                return i

        return -1

s = Solution()
string = "leetcode"
res = s.firstUniqChar(string)
print(res)
