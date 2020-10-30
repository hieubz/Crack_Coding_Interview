# given a sorted array nums, remove the duplicated in-place such that
# each element appears only once and returns the new length
# do not allocate extra space for another array, you must do this by
# modifying the input array in-place with O(1) extra memory

# notice that the array is sorted

class Solution:
    def removeDuplicates(self, nums):
        x = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i + 1]:
                nums[x] = nums[i + 1]
                x += 1

        return x


a = Solution()
res = a.removeDuplicates([1, 1, 2, 3])
print(res)