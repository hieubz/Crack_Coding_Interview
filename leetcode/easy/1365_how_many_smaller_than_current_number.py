# given the array nums, for each nums[i] find out how many numbers in the array are smaller than it
# return the answer in an array

# follow up:
# the given numbers are between 1 and 100

class Solution:
    def smallerNumbersThanCurrent(self, nums):

        dicts = {}

        for index, ele in enumerate(sorted(nums)):
            if ele not in dicts:
                dicts[ele] = index

        return [dicts[num] for num in nums]

    # follow up: we can easily count each number and sum their prefix count
    # O(n)
    def smallerNumbersThanCurrent_2(self, nums):
        count = [0] * 101

        # count
        for num in nums:
            count[num] += 1
        # sum up
        for i in range(1, 101):
            count[i] += count[i - 1]

        # count the numbers are smaller than each element is exactly the previous position's value
        return [count[num - 1] if num != 0 else 0 for num in nums]


    def smallerX(self, nums):
        count = [0] * 101
        for num in nums:
            count[num] += 1

        for i in range(1, 101):
            count[i] += count[i - 1]

        return [count[num - 1] if num != 0 else 0 for num in nums]


s = Solution()
arr = [5, 0, 10, 0, 10, 6]
s.smallerNumbersThanCurrent_2(arr)
