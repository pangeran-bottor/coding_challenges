class Solution:
    def numSplits(self, s: str) -> int:        
        N = len(s)
        left = set()
        right = {}
        for ch in s:
            if ch not in right:
                right[ch] = 0
            right[ch] += 1
        
        ans = 0
        for ch in s:
            left.add(ch)
            right[ch] -= 1
            if right[ch] == 0:
                del right[ch]
            
            if len(left) == len(right):
                ans += 1
        return ans

"""
Using prefix/suffix counter. Might be useful if the question
consists of multiple queries regarding length on left and right.

class Solution:
    def numSplits(self, s: str) -> int:        
        N = len(s)
        left = [0 for _ in range(N)]
        right = [0 for _ in range(N)]
        
        run_set = set()
        for i in range(N):
            run_set.add(s[i])
            left[i] = len(run_set)
        run_set.clear()
        for i in range(N-1, -1, -1):
            run_set.add(s[i])
            right[i] = len(run_set)
        
        ans = 0
        for i in range(N-1):
            if left[i] == right[i+1]:
                ans += 1
        return ans
"""
