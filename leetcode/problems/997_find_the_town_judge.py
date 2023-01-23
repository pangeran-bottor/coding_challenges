from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        n_set = set([i for i in range(1, n + 1)])
        trust_map = {i: [] for i in range(1, n + 1)}
        for p1, p2 in trust:
            trust_map[p2].append(p1)
            if p1 in n_set:
                n_set.remove(p1)

        for candidate, truster in trust_map.items():
            if len(set(truster)) == n - 1 and candidate in n_set:
                return candidate

        return -1
