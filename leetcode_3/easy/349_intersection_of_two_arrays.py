class Solution:
    def intersection(self, nums1, nums2):
        set_2 = set(nums2)

        inter_set = set()

        for number in nums1:
            if number in set_2:
                inter_set.add(number)

        return list(inter_set)
