class Solution:
    def removeDuplicates(self, nums) -> int:

        i = 0
        for number in nums:
            if i < 2 or number > nums[i - 2]:
                nums[i] = number
                i += 1

        return i


s = Solution()
s.removeDuplicates([1, 1, 1, 2, 2, 2, 3])
