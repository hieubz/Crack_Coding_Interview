class Solution:

    # no extra space
    def removeElement(self, nums, val: int) -> int:
        # for i in range(nums.count(val)):
        #     nums.remove(val)

        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1
        print(nums)

        return start


s = Solution()
a = s.removeElement([1, 2, 2, 3, 2], 2)
