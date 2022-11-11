from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # idx
        answer = [0 for _ in range(len(temperatures))]
        
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = idx-prev_day            
            stack.append(idx)
            
        return answer
