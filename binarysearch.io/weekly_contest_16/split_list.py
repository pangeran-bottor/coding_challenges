# https://binarysearch.io/room/Weekly-Contest-16-24956

class Solution:
    def solve(self, nums):
        # Write your code here
        max_from_left = [0] * len(nums)
        min_from_right = [0] * len(nums) 
        
        max_val = float("-inf")
        min_val = float("inf")
        
        for i in range(len(nums)):
            max_val = max(max_val, nums[i])
            max_from_left[i] = max_val
        for i in range(len(nums)-1, -1, -1):
            min_val = min(min_val, nums[i])
            min_from_right[i] = min_val
            
        for i in range(len(nums)-1):
            if max_from_left[i] < min_from_right[i+1]:
                return True
        return False
