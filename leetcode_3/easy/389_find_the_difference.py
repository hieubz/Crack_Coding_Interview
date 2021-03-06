class Solution:
    def findTheDifference(self, s, t):
        result = 0
        for character in s + t:
            result ^= ord(character)

        return chr(result)

