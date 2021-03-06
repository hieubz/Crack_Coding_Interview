class Solution:
    def singleNumber(self, nums) -> int:
        result = 0
        for number in nums:
            result ^= number

        return result
