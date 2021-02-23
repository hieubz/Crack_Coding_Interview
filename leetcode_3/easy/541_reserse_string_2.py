class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        length = len(s)
        s = list(s)
        for i in range(0, length, 2 * k):
            s[i:(i + k)] = s[i:(i + k)][::-1]

        return ''.join(s)
