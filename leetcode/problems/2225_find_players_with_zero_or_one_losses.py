from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lose_map = Counter()
        for winner, loser in matches:
            lose_map[loser] += 1
            lose_map[winner] += 0
        
        not_lost = []
        lost_once = []
        for player, count in lose_map.items():
            if count == 0:
                not_lost.append(player)
            if count == 1:
                lost_once.append(player)
        
        not_lost.sort()
        lost_once.sort()

        return [not_lost, lost_once]
