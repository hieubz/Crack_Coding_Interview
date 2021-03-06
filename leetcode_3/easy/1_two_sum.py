class Solution:
    def twoSum(self, nums, target: int):
        dict = {}

        for i, number in enumerate(nums):
            if target - number in dict:
                return i, dict[target - number]

            dict[number] = i

        return None
