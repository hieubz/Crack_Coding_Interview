class Solution:
    def findTheDifference(self, s, t):
        xor_s = 0
        for c in s + t:
            xor_s ^= ord(c)

        return chr(xor_s)
