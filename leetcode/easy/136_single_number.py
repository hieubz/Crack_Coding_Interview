# given a non-empty array of integers nums, every element appears twice
# except for one. Find that single one

class Solution(object):
    # extra memory
    def singleNumber_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dicts = {}
        for i in nums:
            if i not in dicts:
                dicts[i] = 1
            else:
                del dicts[i]

        return list(dicts.keys())[0]

    def singleNumber_2(self, nums):
        # 2 * (a + b + c) - (a + a + b + b + c) = c
        return 2 * sum(set(nums)) - sum(nums)

    def singleNumber(self, nums):
        # XOR
        a = 0
        for i in nums:
            a ^= i

        return a


s = Solution()
a = s.singleNumber([2, 3, 2, 3, 5])
print(a)
