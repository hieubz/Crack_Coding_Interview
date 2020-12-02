class Solution:
    def insert(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]

        # add all the intervals ending before newInterval starts
        left = [i for i in intervals if i[1] < s]

        # get all the intervals starting after newInterval ends
        right = [i for i in intervals if i[0] > e]

        # need to merge
        if left + right != intervals:
            # merge start
            s = min(s, intervals[len(left)][0])
            # merge end
            e = max(e, intervals[- len(right) - 1][1])

        return left + [[s, e]] + right

    def insert_2(self, intervals, newInterval):
        s, e = newInterval[0], newInterval[1]
        left, right = [], []

        for i in intervals:
            if i[1] < s:
                left.append(i)
            elif i[0] > e:
                right.append(i)
            else:
                # only for clean code but not improve time complexity
                s = min(s, i[0])
                e = max(e, i[1])

        return left + [[s, e]] + right


s = Solution()

a = s.insert([[1, 3], [6, 9]], [2, 5])
print(a)
