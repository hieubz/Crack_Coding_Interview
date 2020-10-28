class Solution:
    def longestCommonPrefix(self, list_str):
        if not list_str:
            return ""

        # sort O(nlog(n))
        shortest_str = sorted(list_str, key=lambda x: len(x))[0]

        # O(n*shortest_length)
        for i, string in enumerate(shortest_str):
            for other in list_str:
                if shortest_str[i] != other[i]:
                    return shortest_str[:i]

        return shortest_str


strs = ['123', '12']
a = Solution()
print(a.longestCommonPrefix(strs))
