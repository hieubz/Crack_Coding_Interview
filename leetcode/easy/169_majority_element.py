# given an array of size n, find the majority element. The majority is the element
# that appears more than [n/2] times.
# assume that the array is non-empty and the majority always exist in the array
from collections import Counter


class Solution:
    def majorityElement(self, nums):
        dict_num = {}
        length = len(nums)
        half = length // 2
        for num in nums:
            if num not in dict_num:
                dict_num[num] = 1
            else:
                dict_num[num] += 1

        for k, v in dict_num.items():
            if dict_num[k] > half:
                return k

    def auto_search(self, nums):
        return Counter(nums).most_common(1)[0][0]


a = [1, 2, 1, 3, 1]
s = Solution()
s.auto_search(a)
