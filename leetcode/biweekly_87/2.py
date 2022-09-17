from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:        
        players.sort(reverse=True)
        trainers.sort(reverse=True)

        ans = 0
        while len(trainers) > 0 and len(players) > 0:
            t = trainers.pop()
            if t < players[-1]:
                pass
            else:
                ans += 1
                players.pop()
        return ans
