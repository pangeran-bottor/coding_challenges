from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans = []

        def insert_interval(cur_interval):
            if len(ans) == 0:
                ans.append(cur_interval)
            else:
                if cur_interval[0] <= ans[-1][1]:
                    ans[-1][1] = max(ans[-1][1], cur_interval[1])
                else:
                    ans.append(cur_interval)

        inserted = False
        for interval in intervals:
            if not inserted and newInterval[0] <= interval[0]:
                insert_interval(newInterval)
                inserted = True

            insert_interval(interval)

        if not inserted:
            insert_interval(newInterval)
        return ans
