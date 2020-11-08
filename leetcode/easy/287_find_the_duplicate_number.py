# given an array of integers nums containing n + 1 integers where each integer is
# in the range [1, n] inclusive.
# There is only one duplicate number in nums, return the duplicate number

class Solution:
    def findDuplicates(self, nums):
        res = []
        for x in nums:
            if nums[abs(x) - 1] < 0:
                #
                res.append(abs(x))
            else:
                # multiply with -1 => turn to negative
                nums[abs(x) - 1] *= -1

        return res


arr = [4, 3, 2, 7, 8, 2, 3, 1]
s = Solution()
s.findDuplicates(arr)

