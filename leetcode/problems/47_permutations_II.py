from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def generate(cur):
            if len(cur) == n:
                arr = tuple([nums[idx] for idx in cur])
                if arr not in seen:
                    seen.add(arr)
                    ans.append(list(arr))
                    return

            for i in range(n):
                if i in cur:
                    continue
                cur.append(i)
                generate(cur)
                cur.pop()

        seen = set()
        n = len(nums)
        ans = []
        generate([])
        return ans
