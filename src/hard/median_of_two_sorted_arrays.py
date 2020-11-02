class Solution:
    def findMedianSortedArrays_lazy(self, nums1, nums2):
        nums1 += nums2
        nums1 = sorted(nums1)
        length = len(nums1)
        if length % 2 != 0:
            return nums1[length // 2]
        else:
            return (nums1[length // 2 - 1] + nums1[length // 2]) / 2

    def merge_sorted_arrays(self, nums1, nums2):

        length_1 = len(nums1)
        length_2 = len(nums2)
        i = length_1 - 1
        j = length_2 - 1
        k = length_1 + length_2 - 1
        nums1 += [0] * length_2

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
                k -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
                k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        while i >= 0:
            nums1[k] = nums1[i]
            k -= 1
            i -= 1

        return nums1

    def findMedianSortedArrays(self, nums1, nums2):

        merged_arr = self.merge_sorted_arrays(nums1, nums2)

        length = len(merged_arr)
        if length % 2 != 0:
            return merged_arr[length // 2]
        else:
            return (merged_arr[length // 2 - 1] + merged_arr[length // 2]) / 2

    # binary search tree version
    def findMedianSortedArrays_bst(self, nums1, nums2):
        pass


if __name__ == '__main__':
    s = Solution()
    a = [1, 2]
    b = [3, 4]
    res = s.findMedianSortedArrays(a, b)
    print(res)
