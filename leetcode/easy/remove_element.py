# 27: given an array nums and a value val, remove all instances of that value in-place
# and return the new length

class Solution:
    def removeElement(self, nums, val):
        # for i in range(nums.count(val)):
        #     nums.remove(val)

        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] == val:
                # swap end and start element, decrease end
                nums[start], nums[end], end = nums[end], nums[start], end - 1
            else:
                start += 1

        return start


nums = [4, 1, 2, 3, 5]
val = 4
s = Solution()
s.removeElement(nums, val)
