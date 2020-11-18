class Solution:
    """sort the array and recursion till got 2 sum"""

    def fourSum(self, nums, target):

        def k_sum(nums, target, k):
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return []
            # when got k == 2 after recursion
            if k == 2:
                return two_sum(nums, target)

            res = []
            for i in range(len(nums)):
                # skip duplicates
                if i == 0 or nums[i - 1] != nums[i]:
                    for pair in k_sum(nums[i + 1:], target - nums[i], k - 1):
                        res.append([nums[i]] + pair)
            return res

        def two_sum(nums, target):
            res = []
            s = {}
            for i in range(len(nums)):
                # check duplicates
                if len(res) == 0 or res[-1][1] != nums[i]:
                    if target - nums[i] in s:
                        res.append([target - nums[i], nums[i]])
                s[nums[i]] = 0

            return res

        nums = sorted(nums)

        return k_sum(nums, target, 4)


nums = [1, 0, -1, 0, -2, 2]
s = Solution()
res = s.fourSum(nums, target=0)
print(res)