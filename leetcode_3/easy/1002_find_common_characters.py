class Solution:
    def commonChars(self, arr):
        check = list(arr[0])
        for word in arr[1:]:
            new_check = []
            for c in word:
                if c in check:
                    new_check.append(c)
                    check.remove(c)
            check = new_check

        return check
