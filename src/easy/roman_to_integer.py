class Solution:

    def __init__(self):
        self.dict_symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
                            'C': 100, 'D': 500, 'M': 1000}

    def romanToInt(self, s: str):

        result = 0
        for i in range(len(s) - 1):
            if self.dict_symbol[s[i]] < self.dict_symbol[s[i + 1]]:
                result -= self.dict_symbol[s[i]]
            else:
                result += self.dict_symbol[s[i]]

        return result + self.dict_symbol[s[-1]]


s = Solution()
print(s.romanToInt('IV'))
