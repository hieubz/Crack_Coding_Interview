class Solution:
    def commonChars(self, arr):
        check = list(arr[0])
        for word in arr[1:]:
            new_check = []
            # check in remain words
            for c in word:
                # if there is any duplicate
                if c in check:
                    new_check.append(c)
                    check.remove(c)

            # keep only duplicate characters
            check = new_check

        return check


s = Solution()
s.commonChars(["bella", "label", "roller"])
