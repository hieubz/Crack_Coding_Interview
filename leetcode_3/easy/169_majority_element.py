class Solution:
    # find the majority element (more than n / 2 times)
    def majorityElement(self, nums) -> int:
        half_len_nums = len(nums) // 2
        num_dict = {}
        for n in nums:
            if n in num_dict:
                num_dict[n] += 1
            else:
                num_dict[n] = 1

        for n, count in num_dict.items():
            if count > half_len_nums:
                return n


x = [3, 2, 3]
s = Solution()
a = s.majorityElement(x)
print(a)
