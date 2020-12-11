class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_nums = set()
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                return True
        return False


s = Solution()
s.containsDuplicate([1, 2, 3, 1])
