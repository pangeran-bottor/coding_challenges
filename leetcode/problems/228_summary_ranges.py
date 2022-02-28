from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        
        result = [[nums[0], None]]
        
        N = len(nums)
        for i in range(1, N):
            target_idx = 0
            if result[-1][1]:
                target_idx += 1
            
            if nums[i]-result[-1][target_idx] == 1:
                result[-1][1] = nums[i]
            else:
                result.append([nums[i], None])
        
        M = len(result)
        for i in range(M):
            if result[i][1]:
                result[i] = "->".join(map(str, result[i]))
            else:
                result[i] = str(result[i][0])
        return result
