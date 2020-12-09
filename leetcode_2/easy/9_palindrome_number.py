# an integer is a palindrome when it reads the same backward as forward

class Solution:
    def isPalindrome_2(self, x: int) -> bool:
        if x >= 0:
            str_x = str(x)
            if str_x == str_x[::-1]:
                return True
            else:
                return False
        else:
            return False

    # solve it without converting the integer to a string
    # but it's too slow
    def isPalindrome(self, x: int) -> bool:
        save = x
        if x >= 0:
            reverse_x = 0
            while x > 0:
                reverse_x = reverse_x * 10 + x % 10
                x = x // 10
            if reverse_x == save:
                return True
            else:
                return False
        else:
            return False

s = Solution()
a = s.isPalindrome(121)
print(a)