class Solution:
    def merge(self, nums1, m, nums2, n) -> list:
        """
        Do not return anything, modify nums1 in-place instead
        :param nums1: array of integers
        :param m:
        :param nums2: array of integers
        :param n:
        :return: merged array
        """

        i = m - 1
        j = n - 1
        k = m + n - 1

        # iterate from last item of array
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                # add to index k
                nums1[k] = nums1[i]
                k -= 1
                i -= 1
            else:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1

        # add remaining parts or nums2
        while j >= 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1

        return nums1

    def merge_2(self, arr1, arr2):
        i = len(arr1) - 1
        j = len(arr2) - 1
        k = i + j + 1
        arr1 += [0] * (j + 1)

        while i >= 0 and j >= 0:
            if arr1[i] > arr2[j]:
                arr1[k] = arr1[i]
                k -= 1
                i -= 1
            else:
                arr1[k] = arr2[j]
                k -= 1
                j -= 1

        while j >= 0:
            arr1[k] = arr2[j]
            k -= 1
            j -= 1

        return arr1




if __name__ == '__main__':
    s = Solution()
    a = [1, 2, 3, 9]

    b = [2, 5, 6]
    merged_arr = s.merge_2(a, b)
    print(merged_arr)
