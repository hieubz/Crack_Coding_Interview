#  you are given an integer array nums sorted in ascending order and an integer target
#  suppose that nums is rotated at some pivot unknown to you beforehand
# if target is found in the array return its index, otherwise return -1

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # ensure we are searching on sorted array (because it was rotated)
            # => check left and right and search on sorted part
            # left rotated
            if nums[mid] >= nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                # right rotated
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1


s = Solution()
arr = [-1, 0, 3, 5, 9, 12]
res = s.search(arr, 2)
print(res)
