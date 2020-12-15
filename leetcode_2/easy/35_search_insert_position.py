class Solution:
    # sorted array nums
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            else:
                return mid

        return l


s = Solution()
a = s.searchInsert([1, 3, 3, 5, 5, 10], 4)
print(a)