from typing import List, Tuple, DefaultDict
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans: DefaultDict[Tuple, List[str]] = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())
