from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        def substract_vecs(vec1, vec2):
            new_vec = list(vec1)
            for i in range(26):
                new_vec[i] -= vec2[i]
            return new_vec
        
        def is_equal_vec(vec1, vec2):
            for i in range(26):
                if vec1[i] != vec2[i]:
                    return False
            return True
        
        p_vec = [0] * 26
        for ch in p:
            p_vec[ord(ch)-97] += 1
        result = []
        maps = [[0]*26]
        for ch in s:
            new_vec = list(maps[-1])
            new_vec[ord(ch)-97] += 1
            maps.append(new_vec)

        for i in range(len(p), len(maps)):
            diff_vec = substract_vecs(maps[i], maps[i-len(p)])

            if is_equal_vec(diff_vec, p_vec):
                result.append(i-len(p))
            
        return result
