# palindromic string is a string that equals to its reverse string

class Solution:
    def longestPalindrome(self, s):

        rev = ""
        for i in range(len(s)):
            # odd case, like 'aba'
            tmp = self.helper(s, i, i)
            if len(tmp) > len(rev):
                rev = tmp

            # even case, like 'abba'
            tmp = self.helper(s, i, i + 1)
            if len(tmp) > len(rev):
                rev = tmp

        return rev

    def helper(self, s, l, r):
        """
        check palindrome number with 2 indexes forward and backward
        :param s:
        :param l:
        :param r:
        :return:
        """
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1

        return s[(l + 1): r]


a = Solution()
rev = a.longestPalindrome('abcb')
print(rev)
