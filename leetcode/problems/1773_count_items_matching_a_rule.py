from typing import List


class Solution:
    def countMatches(self,
                     items: List[List[str]],
                     ruleKey: str,
                     ruleValue: str) -> int:
        ruleKeyIdx = {"type": 0, "color": 1, "name": 2}
        ans = 0
        for item in items:
            if item[ruleKeyIdx[ruleKey]] == ruleValue:
                ans += 1
        return ans
