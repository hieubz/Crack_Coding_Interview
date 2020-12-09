class Solution:
    def reverse(self, x: int) -> int:
        a = 0
        negative = 1
        if x < 0:
            negative = -1
            x = abs(x)

        while x > 0:
            a = a * 10 + x % 10
            x = x // 10

        if a > pow(2, 31):
            return 0

        return a * negative

    def reverse_2(self, x):
        str_x = str(x)
        reverse_int = int(str_x[::-1]) if str_x[0] != '-' else -int(str_x[:0:-1])

        if abs(reverse_int) >= 2**31:
            return 0

        return reverse_int
