from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome_partition(partition):
            for s in partition:
                for i in range(len(s) // 2):
                    if s[i] != s[len(s) - i - 1]:
                        return False
            return True

        def generate(start, cur):
            if start == n and is_palindrome_partition(cur):
                cur = ["".join(p) for p in cur]
                ans.append(list(cur))
                return

            for i in range(start, n):
                cur.append(s[start : i + 1])
                generate(i + 1, cur)
                cur.pop()

        s = list(s)
        n = len(s)
        ans = []
        generate(0, [])

        return ans
