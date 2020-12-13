class Solution:

    # O2n
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_chars = set()
        result = 0

        i, j = 0, 0
        length = len(s)

        while i < length and j < length:
            if s[j] not in set_chars:
                set_chars.add(s[j])
                j += 1
                result = max(result, j - i)
            else:
                set_chars.remove(s[i])
                i += 1

        return result

    def lengthOfLongestSubstring_2(self, s: str) -> int:
        dct_chars = {}
        result = 0
        i, j = 0, 0
        length = len(s)

        for j in range(length):
            if s[j] in dct_chars:
                i = max(i, dct_chars[s[j]])

            result = max(result, j - i + 1)
            dct_chars[s[j]] = j + 1

        return result


s = Solution()
print(s.lengthOfLongestSubstring_2("tmmzuxt"))
