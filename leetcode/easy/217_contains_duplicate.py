# given an array of integers, find if the array contains any duplicates
# return true if any value appears at least twice in the array
# return false if every element is distinct

class Solution:
    def containsDuplicate(self, nums):
        dict_num = {}
        for i in nums:
            if i not in dict_num:
                dict_num[i] = 0
            else:
                return True

        return False
