from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        n = len(box[0])

        for row in box:
            last_idx = n
            for i in range(n - 1, -1, -1):
                if row[i] == "*":
                    last_idx = i
                elif row[i] == "#":
                    if i != last_idx - 1:
                        row[last_idx - 1] = "#"
                        row[i] = "."
                    last_idx -= 1

        ans = []
        for col in range(n):
            # iterate the box in reverse
            ans.append([row[col] for row in box[::-1]])
        return ans
