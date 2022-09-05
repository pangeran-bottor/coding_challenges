from typing import List


class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        pos_map = {}
        for ch in alphabets:
            pos_map[ch] = []
        
        for idx, ch in enumerate(s):
            pos_map[ch].append(idx)
            
        for idx, el in enumerate(distance):
            if len(pos_map[alphabets[idx]]) == 0:
                continue
            
            l, r = pos_map[alphabets[idx]]
            if r-l-1 != el:
                return False
        return True
