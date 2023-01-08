from typing import List


class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        max_damage = max(damage)
        sum_damage = sum(damage)
        return 1 + sum_damage - min(armor, max_damage)
