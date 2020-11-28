# given a list of strings arr representing an English Dict, find the longest word in arr
# that can be built one character at a time by other words in arr.

class Solution:
    # O w * l
    def longestWord(self, words):
        ans = ""
        wordset = set(words)
        for word in words:
            if len(word) >= len(ans) and word < ans:
                if all(word[:k] in wordset for k in range(len(word))):
                    ans = word

        return ans
