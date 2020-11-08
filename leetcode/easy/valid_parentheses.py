class Solution:

    def __init__(self):
        self.char_dict = {')': "(", '}': '{', ']': '['}

    def isValid(self, s: str):
        stack = []
        for char in s:
            if char in self.char_dict:
                top_element = stack.pop() if stack else '#'
                if self.char_dict[char] != top_element:
                    return False

            else:
                stack.append(char)

        return not stack


s = Solution()
print(s.isValid('()[]'))
