from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        ans = 0
        cur_max = cur_sum = neededTime[0]

        for i in range(1, len(colors)):
            if colors[i - 1] == colors[i]:
                cur_max = max(cur_max, neededTime[i])
                cur_sum += neededTime[i]
            else:
                ans += cur_sum - cur_max
                cur_max = cur_sum = neededTime[i]

        return ans + (cur_sum - cur_max)
