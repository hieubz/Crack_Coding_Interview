# given a non-empty array of integers, return the k most frequent elements
from collections import Counter


class Solution:
    def topKFrequent(self, nums, k: int):
        count = Counter(nums)

        return [ele[0] for ele in count.most_common(k)]

    def topKFrequent_2(self, nums, k):
        dicts = {}
        for num in nums:
            if num not in dicts:
                dicts[num] = 1
            else:
                dicts[num] += 1

        arr = [0] * len(dicts)
        if len(dicts) == 1:
            return dicts.keys()
        for num, counts in dicts.items():
            arr[num] = counts - 1

        return arr[-k:]
    #
    # # Quick select is an algorithm typically used to solve the problems
    # # "find k th something": k th smallest, k th largest, k th most frequent
    # # k th less frequent
    # # O(n) average time complexity and widely used in practice
    # # the approach is the same as for quicksort
    #
    # def topKFrequent_2(self, nums, k):
    #     # split array into two parts


s = Solution()
arr = [1, 2]
s.topKFrequent_2(arr, 2)
