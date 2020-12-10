class Solution:

    def __init__(self):
        self.brackets = {']': '[', '}': '{', ')': '('}

    def isValid(self, s: str) -> bool:
        if not s:
            return False

        stack = []
        for character in s:
            if character in ['[', '{', '(']:
                stack.append(character)
            else:
                if self.brackets[character] != stack.pop() if stack else '#':
                    return False

        return not stack


s = Solution()
print(s.isValid("()"))
