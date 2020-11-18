class Solution:
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1

        return l

    def searchInsert_2(self, nums, target):  # works even if there are duplicates.
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            else:
                if nums[mid] == target and nums[mid - 1] != target:
                    return mid
                else:
                    r = mid - 1
        return l


a = [3, 4, 4, 5, 6]
s = Solution()
res = s.searchInsert_2(a, 4)
print(res)
