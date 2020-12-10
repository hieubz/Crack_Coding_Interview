class Solution:
    def removeDuplicates(self, nums) -> int:
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1

        return x


s = Solution()
print(s.removeDuplicates([1, 1, 2]))
