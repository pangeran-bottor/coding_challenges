from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def _generate(num: int, curr: List[int]):
            if len(curr) == k:
                ans.append(list(curr))
                return

            # n - num + 1, since we include num as the first element
            # k - len(curr), count of what we need to finish
            available = (n - num + 1) - (k - len(curr))
            for i in range(num, num + available + 1):
                curr.append(i)
                _generate(i + 1, curr=curr)
                curr.pop()

        ans: List[List[int]] = []
        _generate(1, [])
        return ans


if __name__ == "__main__":
    n, k = 4, 2
    for c in Solution().combine(n, k):
        print(c)
