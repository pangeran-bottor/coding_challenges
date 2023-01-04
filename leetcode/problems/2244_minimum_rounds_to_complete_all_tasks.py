from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        difficulty_counts = {}
        for difficulty in tasks:
            if difficulty not in difficulty_counts:
                difficulty_counts[difficulty] = 0
            difficulty_counts[difficulty] += 1

        rounds = 0
        for difficulty, count in difficulty_counts.items():
            if count == 1: return -1
            if count % 3 == 0:
                rounds += (count//3)
            elif count % 3 == 1:
                rounds += ((count-4)//3) + 2
            elif count % 3 == 2:
                rounds += (count//3) + 1
            
        return rounds
