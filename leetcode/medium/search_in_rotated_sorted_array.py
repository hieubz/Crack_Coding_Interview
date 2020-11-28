#  you are given an integer array nums sorted in ascending order and an integer target
#  suppose that nums is rotated at a unknown pivot to you beforehand
# if target is found in the array return its index, otherwise return -1

class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid

            # ensure we are searching on sorted array (because it was rotated)
            # => check left and right and search on sorted part

            # left is normally ordered
            if nums[mid] >= nums[l]:
                # search left
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            else:
                # right is normally ordered
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return -1

    def search_1(self, array, target):
        l = 0
        r = len(array) - 1

        while l <= r:
            mid = (l + r) // 2
            if array[mid] == target:
                return mid

            # left is normally sorted
            if array[mid] >= array[l]:
                if array[l] <= target < array[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                # right is normally sorted
                if array[mid] < target <= array[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return -1

    # recursion
    def search_2(self, arr, x, left, right):
        mid = (left + right) // 2
        if x == arr[mid]:
            return mid

        if right < left:
            return -1

        if arr[mid] > arr[left]:
            if arr[left] <= x < arr[mid]:
                return self.search_2(arr, x, left, mid - 1)
            else:
                return self.search_2(arr, x, mid + 1, right)
        elif arr[mid] < arr[left]:
            if arr[mid] < x <= arr[right]:
                return self.search_2(arr, x, mid + 1, right)
            else:
                return self.search_2(arr, x, left, mid - 1)
        else:
            # arr[mid] = arr[left] => left or right half is all repeats
            if arr[mid] != arr[right]:
                return self.search_2(arr, x, mid + 1, right)
            else:
                # have to search both halves
                result = self.search_2(arr, x, left, mid - 1)
                if result == -1:
                    return self.search_2(arr, x, mid + 1, right)
                else:
                    return result


s = Solution()
arr = [3, 5, 9, 12, 0, 1, 2]
res = s.search_2(arr, 2, 0, 6)
print(res)
