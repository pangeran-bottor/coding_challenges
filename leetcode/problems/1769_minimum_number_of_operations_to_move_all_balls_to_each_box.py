from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        prefix_list = [0] * N
        suffix_list = [0] * N

        count = 0
        for i in range(N):
            if i != 0:
                prefix_list[i] += (prefix_list[i-1] + count)
            if int(boxes[i]) == 1:
                count += 1

        count = 0
        for i in range(N-1, -1, -1):
            if i != N-1:
                suffix_list[i] += (suffix_list[i+1] + count)
            if int(boxes[i]) == 1:
                count += 1
        ans = [el[0] + el[1] for el in zip(prefix_list, suffix_list)]
        return ans
