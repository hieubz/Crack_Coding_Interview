from xmlrpc.client import MAXINT, MININT


class Solution:
    # def myAtoi(self, s):
    #     s = list(s)
    #     for i in range(len(s)):
    #         if s[i] != ' ':
    #             s = s[i:]
    #             break
    #
    #     if len(s) == 0:
    #         return 0
    #
    #     if s[0].isdigit():
    #         j = 1
    #         for i in s[1:]:
    #             if i.isdigit():
    #                 j += 1
    #             else:
    #                 break
    #         s = int(''.join(s[:j]))
    #         if s <= MAXINT:
    #             return s
    #         else:
    #             return MAXINT
    #
    #     elif s[0] == '-' or s[0] == '+':
    #         j = 1
    #         for i in s[1:]:
    #             if i.isdigit():
    #                 j += 1
    #             else:
    #                 break
    #         if len(s[:j]) > 1:
    #             s = - int(''.join(s[1:j])) if s[0] == '-' else + int(''.join(s[1:j]))
    #         else:
    #             return 0
    #
    #         if s < 0:
    #             if s >= MININT:
    #                 return s
    #             else:
    #                 return MININT
    #         else:
    #             if s <= MAXINT:
    #                 return s
    #             else:
    #                 return MAXINT
    #
    #     else:
    #         return 0

    def myAtoi(self, s):
        indicator = 1
        result = 0
        s = list(s)
        for i in range(len(s)):
            if s[i] != ' ':
                s = s[i:]
                break

        if len(s) == 0:
            return 0

        i = 0
        if s[i] == '-' or s[i] == '+':
            indicator = -1 if s[i] == '-' else 1
        i += 1
        while s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
            if result * indicator >= MAXINT:
                return MAXINT
            if result * indicator <= MININT:
                return MININT

            return result * indicator


s = Solution()
print(s.myAtoi('42'))
