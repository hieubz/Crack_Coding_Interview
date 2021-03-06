class Solution:
    def containsDuplicate(self, nums) -> bool:
        set_num = set()
        for number in nums:
            if number in set_num:
                return True
            set_num.add(number)

        return False
