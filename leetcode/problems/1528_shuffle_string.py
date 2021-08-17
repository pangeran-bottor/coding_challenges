from typing import List


class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ans_list = [""] * (len(s))
        for i in range(len(s)):
            ans_list[indices[i]] = s[i]
        ans = "".join(ans_list)
        return ans
