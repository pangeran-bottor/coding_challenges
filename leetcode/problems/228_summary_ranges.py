from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        N = len(nums)
        ans = []

        for num in nums:
            if not ans or num > ans[-1][-1] + 1:
                ans.append([num])
            elif len(ans[-1]) == 1:
                ans[-1].append(num)
            else:
                ans[-1][-1] = num

        return ["->".join(map(str, el)) for el in ans]
