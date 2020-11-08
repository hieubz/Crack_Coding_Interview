# given an array of integers and an integer k, find out whether there are two distinct indices
# i and j in the array such that nums[i] = nums[j] and the absolute difference between
# i and j is at most k

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        dict_num = {}
        for i, num in enumerate(nums):
            if num in dict_num and i - dict_num[num] <= k:
                return True
            # update index for num whether it exists in the dict or not
            dict_num[num] = i

        return False


s = Solution()
result = s.containsNearbyDuplicate([1, 0, 1, 1], 1)

print(result)
