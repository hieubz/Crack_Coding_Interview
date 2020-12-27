from collections import Counter


class Solution:
    # find the majority element (more than n / 2 times)
    def majorityElement(self, nums):
        count = Counter(nums)
        half = len(nums) // 2

        num, value = count.most_common(1)[0]

        if value > half:
            print(num)
            return num

        return -1


s = Solution()
s.majorityElement([1, 2, 2, 3, 2])
