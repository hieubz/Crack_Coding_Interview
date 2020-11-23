# count the number of prime numbers less than a non-negative number n
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0

        s = [1] * n

        s[0] = s[1] = 0

        for i in range(2, n // 2 + 1):
            if s[i]:
                for j in range(i * i, n, i):
                    s[j] = 0

        return sum(s)


s = Solution()
a = s.countPrimes(10)
print(a)
