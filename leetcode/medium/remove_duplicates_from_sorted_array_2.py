# given a sorted array nums, remove the duplicated in-place such that
# each element appears only once and returns the new length
# do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory

# notice that the array is sorted
# instead of using a 1-window, we use 2-window

class Solution:
    def removeDuplicates(self, nums):
        i = 0
        for number in nums:
            if i < 2 or number > nums[i-2]:
                nums[i] = number
                i += 1

        return i


a = Solution()
res = a.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 2, 3, 3])
print(res)
