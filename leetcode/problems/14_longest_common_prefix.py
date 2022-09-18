from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        
        sample = strs.pop()
        if len(strs) == 0:
            return sample
        
        for idx, ch in enumerate(sample):
            is_valid = True
            for word in strs:
                if len(word)-1 < idx or word[idx] != ch:
                    is_valid = False
                    break
            if not is_valid:
                break
            ans += ch
        return ans
