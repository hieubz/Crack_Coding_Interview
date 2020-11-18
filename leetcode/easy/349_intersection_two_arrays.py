class Solution:

    # hashmap is the best
    # O(n +m)
    def intersection(self, nums1, nums2):
        dicts = {}
        for i in nums1:
            if i not in dicts:
                dicts[i] = 1

        result = []

        for i in nums2:
            if i in dicts:
                result.append(i)

        return set(result)

    # O(m + n) but time space O(1)
    # sorted array assumption
    def intersection_2(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        result = []
        for i in nums1:
            if i in nums2:
                result.append(i)

        return result
