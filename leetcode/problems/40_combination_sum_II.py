from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def generate(idx, cur):
            if sum(cur) == target:
                ans.add(tuple(cur))
                return

            if sum(cur) > target:
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                cur.append(candidates[i])
                generate(i + 1, cur)
                cur.pop()

        n = len(candidates)
        candidates.sort()
        ans = set()
        generate(0, [])
        return list(ans)
