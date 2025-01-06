from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        cur_count, cur_sum = 0, 0
        ans = [0 for _ in range(n)]

        for i in range(n):
            ans[i] += cur_count + cur_sum
            cur_sum += cur_count
            if boxes[i] == "1":
                cur_count += 1

        cur_count, cur_sum = 0, 0
        for i in range(n):
            ans[n - i - 1] += cur_count + cur_sum
            cur_sum += cur_count
            if boxes[n - i - 1] == "1":
                cur_count += 1

        return ans
