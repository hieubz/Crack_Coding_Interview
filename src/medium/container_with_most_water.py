class Solution:
    def maxArea(self, height):
        l, r, width, res = 0, len(height) - 1, len(height) - 1, 0
        # go backward
        for w in range(width, 0, -1):
            # compare and go forward
            if height[l] < height[r]:
                res, l = max(res, height[l] * w), l + 1
            else:
                res, r = max(res, height[r] * w), r - 1


if __name__ == '__main__':
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    s = Solution()
    s.maxArea(height)
