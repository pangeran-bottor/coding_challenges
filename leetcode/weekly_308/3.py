# https://leetcode.com/contest/weekly-contest-308/problems/minimum-amount-of-time-to-collect-garbage/

from typing import List


def calculate(garbage_type, garbage, travel):
    result = 0
    
    last_idx = -1
    task = 0
    for idx, g in enumerate(garbage):
        count = g.count(garbage_type)
        if count > 0:
            result += count
            last_idx = idx
            task += 1
    
    if task > 0 and last_idx > 0:
        result += travel[last_idx-1]
    return result
            
    

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        for i in range(1, len(travel)):
            travel[i] += travel[i-1]

        result = 0
        for garbage_type in ("P", "M", "G"):
            result += calculate(garbage_type, garbage, travel)
        return result
