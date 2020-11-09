# given an array nums of n integers and an integer target
# find three integers in nums such that the sum is closest to target
# return the sum of the three integers

class Solution:
    def threeSumClosest(self, nums, target):
        # with sum issues => always sort array first
        nums = sorted(nums)
        result = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            start, end = i + 1, len(nums) - 1
            while start < end:
                sums = nums[i] + nums[start] + nums[end]
                # larger than target => backward
                if sums > target:
                    end -= 1
                else:
                    # smaller than target => go forward
                    start += 1

                # update new smaller sum
                if abs(sums - target) < abs(result - target):
                    result = sums

        return result
