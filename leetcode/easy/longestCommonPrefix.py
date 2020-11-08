class Solution:
    def longestCommonPrefix(self, list_str):
        if not list_str:
            return ""

        # # sort O(nlog(n))
        # shortest_str = sorted(list_str, key=lambda x: len(x))[0]

        # O(n*shortest_length)
        for i, char in enumerate(list_str[0]):
            for other in list_str:
                if i == len(other) or char != other[i]:
                    return list_str[0][:i]

        return list_str[0]


strs = ['123', '12']
a = Solution()
print(a.longestCommonPrefix(strs))
