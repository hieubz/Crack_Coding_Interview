from xmlrpc.client import MAXINT, MININT


class Solution:

    # O(n)
    def reverse(self, x: int) -> int:
        str_x = str(x)
        x = int(str_x[::-1]) if str_x[0] != '-' else -int(str_x[:0:-1])
        if abs(x) < 2 ** 31:
            return x
        else:
            return 0

    # O(log(n))
    def reverse_2(self, x: int):
        rev = 0
        while x != 0:
            rev = rev * 10 + x % 10
            if rev > MAXINT or rev < MININT:
                return 0
            x = x // 10

        return rev


s = Solution()
print(s.reverse_2(1534236))
