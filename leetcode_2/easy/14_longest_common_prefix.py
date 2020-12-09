# write a function to find the longest common prefix string

class Solution:
    def longestCommonPrefix(self, strs) -> str:
        for i, char in enumerate(strs[0]):
            for other in strs[1:]:
                if i == len(other) or char != other[i]:
                    return strs[0][:i]

        return strs[0]
