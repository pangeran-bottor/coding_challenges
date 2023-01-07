from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        cur_gas = 0
        start_idx = 0
        n = len(gas)
        for i in range(n):
            cur_gas += gas[i] - cost[i]
            if cur_gas < 0:
                start_idx = i + 1
                cur_gas = 0
        return start_idx
