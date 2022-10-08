from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def encode(word):
            arr = [0 for _ in range(26)]
            for ch in word:
                arr[ord(ch)-ord("a")] += 1
            return arr
        
        def is_subset(base, target):
            for idx, ct in enumerate(target):
                if ct > 0 and base[idx] < ct:
                    return False
            return True
        
        target = [0 for _ in range(26)]
        for word in words2:
            encoded = encode(word)
            for i in range(26):
                target[i] = max(target[i], encoded[i])
        
        ans = []
        for word in words1:
            encoded = encode(word)
            if is_subset(encoded, target):
                ans.append(word)
        return ans
