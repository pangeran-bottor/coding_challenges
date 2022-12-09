from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill.sort()
        target = sum(skill) // (n//2)
        
        ans = 0
        for i in range(n//2):
            left = skill[i]
            right = skill[n-1-i]
            if left + right != target:
                return -1
            else:
                ans += (left * right)
        return ans
