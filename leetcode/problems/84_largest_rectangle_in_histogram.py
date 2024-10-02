from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)
        stack = []

        for idx, h in enumerate(heights):
            start_idx = idx
            while stack and stack[-1][-1] > h:
                prev_idx, prev_h = stack.pop()
                ans = max(ans, prev_h * (idx - prev_idx))
                start_idx = prev_idx
            stack.append((start_idx, h))

        while stack:
            idx, h = stack.pop()
            ans = max(ans, h * (n - idx))

        return ans
