class Solution:
    def partitionString(self, s: str) -> int:
        ans = 1
        cur_set = set()

        for ch in s:
            if ch in cur_set:
                ans += 1
                cur_set = set({ch})
            else:
                cur_set.add(ch)

        return ans
