class Solution:
    def commonChars(self, arr):
        first_s = list(arr[0])
        for s in arr[1:]:
            new_check = []
            for character in s:
                if character in first_s:
                    new_check.append(character)
                    first_s.remove(character)

            first_s = new_check

        return first_s

