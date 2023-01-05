from functools import cache


class Solution:
    def numTrees(self, n: int) -> int:
        @cache
        def iterate(start, end):
            if start > end:
                return 1

            count = 0
            for i in range(start, end + 1):
                left_trees = iterate(start, i - 1)
                right_trees = iterate(i + 1, end)
                count += left_trees * right_trees

            return count

        return iterate(1, n)
