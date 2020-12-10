class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        merged_arr = self.merge(nums1, nums2)
        leng = len(merged_arr)
        if leng % 2 == 0:
            return (merged_arr[leng // 2] + merged_arr[leng // 2 + 1]) / 2
        else:
            return float(merged_arr[leng // 2])

    def merge(self, l1, l2):
        len1 = len(l1)
        len2 = len(l2)

        i, j = len1 - 1, len2 - 1
        k = len1 + len2 - 1
        l1 += [0] * len2
        while i >= 0 and j >= 0:
            if l1[i] >= l2[j]:
                l1[k] = l1[i]
                k -= 1
                i -= 1
            else:
                l1[k] = l2[j]
                k -= 1
                j -= 1

        while j >= 0:
            l1[k] = l2[j]
            k -= 1
            j -= 1

        return l1
