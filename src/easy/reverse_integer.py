class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(x)
        x = int(str_x[::-1]) if str_x[0] != '-' else -int(str_x[:0:-1])
        if abs(x) < 2**31:
            return x
        else:
            return 0


s = Solution()
print(2**31)
s.reverse(1534236469)
