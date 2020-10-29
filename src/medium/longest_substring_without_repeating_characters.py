# given a string s, find the length of the longest substring
# without repeating characters

class Solution:
    def lengthOfLongestSubstring(self, s: str):
        s = list(s)
        dict_s = {}
        answer = 0

        # index for get the length of the longest substring
        i = 0
        for j, char in enumerate(s):
            index = dict_s.get(char)
            # if it has repeating character => update current first index
            if index:
                i = max(dict_s[char], i)

            # get the length from current first index i
            # get max from start to avoid sorting task when finishing
            answer = max(answer, j - i + 1)
            # add char to dict (count from 1)
            dict_s[char] = j + 1

        return answer


s = Solution()
res = s.lengthOfLongestSubstring("abcabcbb")
print(res)