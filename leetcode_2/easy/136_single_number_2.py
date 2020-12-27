class Solution:
    def singleNumber(self, nums):
        return sum(set(nums)) * 2 - 2 * sum(nums)

    def singleNumber_2(self, nums):
        res = 0

        for i in nums:
            res ^= i

        return res
