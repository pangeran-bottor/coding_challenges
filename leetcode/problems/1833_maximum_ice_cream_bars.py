from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        for i in range(1, len(costs)):
            costs[i] += costs[i - 1]

        if coins < costs[0]:
            return 0
        if sum(costs) <= coins:
            return len(costs)

        l, r = 0, len(costs) - 1

        ans = 0
        while l <= r:
            mid = (l + r) // 2
            if costs[mid] == coins:
                ans = mid + 1
                break
            elif costs[mid] > coins:
                r = mid - 1
            else:
                ans = max(ans, mid + 1)
                l = mid + 1
        return ans
