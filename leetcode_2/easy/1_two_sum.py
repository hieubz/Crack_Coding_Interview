class Solution:
    def twoSum(self, nums, target: int):
        dicts = {}
        for index, num in enumerate(nums):
            if target - num in dicts:
                return [index, dicts[target - num]]
            if num not in dicts:
                dicts[num] = index


s = Solution()
a = s.twoSum([2, 7, 11, 15], 9)
print(a)