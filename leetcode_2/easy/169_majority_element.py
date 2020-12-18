from collections import Counter


class Solution:
    # find the majority element (more than n / 2 times)
    def majorityElement(self, nums) -> int:
        count = Counter(nums)
        half = len(nums) // 2
        for k, v in count.items():
            if v > half:
                return k
