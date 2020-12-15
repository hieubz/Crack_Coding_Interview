class Solution:
    def maxArea(self, height) -> int:
        length = len(height)
        max_res = 0
        for k, h in enumerate(height):
            for j in range(k, length):
                square = (j - k) * min(h, height[j])
                if max_res < square:
                    max_res = square

        return max_res

    def maxArea_2(self, height):
        l, r = 0, len(height) - 1
        max_res = 0

        while l < r:
            if height[l] < height[r]:
                max_res = max(max_res, height[l] * (r - l))
                l += 1
            else:
                max_res = max(max_res, height[r] * (r - l))
                r -= 1

        return max_res
