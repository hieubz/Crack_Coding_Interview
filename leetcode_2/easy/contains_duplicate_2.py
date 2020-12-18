class Solution:
    def containsNearbyDuplicate(self, nums, k: int) -> bool:
        dict_num = {}
        for i, num in enumerate(nums):
            if num in dict_num and i - dict_num[num] <= k:
                return True
            dict_num[num] = i

        return False
