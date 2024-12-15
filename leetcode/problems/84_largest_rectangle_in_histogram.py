from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        ans = 0
        for idx, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                top_idx = stack.pop()
                width = idx if not stack else idx - stack[-1] - 1
                ans = max(ans, heights[top_idx] * width)
            stack.append(idx)
        return ans
