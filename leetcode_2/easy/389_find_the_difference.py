class Solution:

    # get ASCII value by ord
    # return character from ASCII value by chr

    def findTheDifference(self, s, t):
        code = 0
        for char in s + t:
            code ^= ord(char)

        return chr(code)
