from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = 0
        solution_set = set()
        visited_set = set()
        
        for num in nums:
            target_1 = num + k
            target_2 = num - k
            
            if target_1 in visited_set:
                if (num, target_1) not in solution_set and (target_1, num) not in solution_set:
                    result += 1
                    solution_set.add((num, target_1))
            if target_2 in visited_set:
                if (num, target_2) not in solution_set and (target_2, num) not in solution_set:
                    result += 1
                    solution_set.add((num, target_2))
            
            visited_set.add(num)
        return result
