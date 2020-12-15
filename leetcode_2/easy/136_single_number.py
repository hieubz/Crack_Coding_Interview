class Solution:
    def singleNumber(self, nums) -> int:
        a = 0
        for i in nums:
            a ^= i

        return a
