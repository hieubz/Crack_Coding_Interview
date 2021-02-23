class Solution:
    # no extra space
    def removeElement(self, nums, val: int) -> int:
        # count = 0
        # for n in nums:
        #     if n == val:
        #         count += 1
        #
        # for i in range(count):
        #     nums.remove(val)

        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] <= end:
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1

        return start
