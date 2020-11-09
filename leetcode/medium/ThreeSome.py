# given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0
# Find all unique triplets in the array which gives the sum of zero

class Solution:
    def threeSum(self, nums):
        if not nums or len(nums) < 3:
            return []
        nums = sorted(nums)

        if nums[0] > 0:
            return []

        length = len(nums)
        result = []
        for i, number in enumerate(nums):
            # first element or ...
            if i == 0 or (i > 0 and number != nums[i - 1]):
                start = i + 1
                end = length - 1
                sum = 0 - number
                while start < end:
                    if nums[start] + nums[end] == sum:
                        # append to result array
                        result.append((nums[start], nums[end], number))

                        # remove duplicates
                        while start < end and nums[start] == nums[start + 1]:
                            start += 1
                        while start < end and nums[end] == nums[end - 1]:
                            end -= 1

                        # continue with next index
                        start += 1
                        end -= 1

                    # not enough
                    elif nums[start] + nums[end] < sum:
                        start += 1
                    else:
                        # larger than sum => backward
                        end -= 1

        return result

    def twoSum(self, nums):
        result = []
        dict_int = {}
        if not nums or len(nums) < 2:
            return []

        # O(n) with nums contains only distinct integers
        for i in nums:
            dict_int[i] = 0
        for i in nums:
            if -i in dict_int:
                result.append((i, -i))

        return result
