from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color: dict[int, int] = {}
        color_count: dict[int, int] = {}

        ans = []
        for ball, color in queries:
            if ball in ball_color:
                prev_color = ball_color[ball]
                color_count[prev_color] -= 1
                if color_count[prev_color] == 0:
                    del color_count[prev_color]
            ball_color[ball] = color
            color_count[color] = color_count.get(color, 0) + 1

            ans.append(len(color_count))
        return ans
