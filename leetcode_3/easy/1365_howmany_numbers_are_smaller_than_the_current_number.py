class Solution:
    def smallerNumbersThanCurrent(self, nums):
        count = [0] * 101

        for number in nums:
            count[number] += 1

        for i in range(0, 100):
            count[i + 1] += count[i]

        return [count[number - 1] if number > 0 else 0 for number in nums]
