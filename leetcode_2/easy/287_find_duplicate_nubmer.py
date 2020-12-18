class Solution:
    def findDuplicate(self, nums) -> int:
        dicts = {}
        for i in nums:
            if i not in dicts:
                dicts[i] = 0
            else:
                return i
