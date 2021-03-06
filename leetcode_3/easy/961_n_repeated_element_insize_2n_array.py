class Solution:
    def repeatedNTimes(self, A):
        set_num = set()
        for number in A:
            if number not in set_num:
                set_num.add(number)
            else:
                return number

        return None