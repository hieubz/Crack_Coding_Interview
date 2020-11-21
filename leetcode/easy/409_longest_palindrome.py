# given a string s, return the length of the longest palindrome that can be
# built with those letters
import collections


class Solution:
    def longestPalindrome(self, s):
        dicts = {}
        for i in s:
            if i in dicts:
                dicts[i] = 1
            else:
                dicts[i] += 1

        result = 0
        for v in dicts.values():
            # for each letter, say it occurs v times. We know we have v // 2 * 2 letters
            # that can be partnered for sure.
            # for example, if we have 'aaaaa', we can have 'aaaa' partnered, which is 5 // 2 * 2 = 4
            # letters partnered
            result += v // 2 * 2

            # if there was any v % 2 == 1
            # then that letter could be a unique center.
            # so I can increase result by 1 (only one time)

            if result % 2 == 0 and v % 2 == 1:
                result += 1

        return result


class Solution_2:
    def longestPalindrome(self, s):
        ans = 0
        for v in collections.Counter(s).values():
            ans += v / 2 * 2
            if ans % 2 == 0 and v % 2 == 1:
                ans += 1
        return ans


s = Solution()
res = s.longestPalindrome("abccccdd")
print(res)