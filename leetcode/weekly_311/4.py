from typing import List


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:

        # TODO: optimize using Trie and prefix sum

        pre_map = {}
        for word in words:
            key = ""
            for ch in word:
                key += ch
                if key not in pre_map:
                    pre_map[key] = 0
                pre_map[key] += 1
        ans = []
        for word in words:
            val = 0
            key = ""
            for ch in word:
                key += ch
                val += pre_map[key]
            ans.append(val)
        return ans
