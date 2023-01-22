from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partitions = set()
        seq = []
        n = len(s)

        def is_palindrome_partition(p):
            for el in p:
                el_len = len(el)
                for i in range(el_len // 2):
                    if el[i] != el[el_len - i - 1]:
                        return False
            return True

        def backtrack(idx):
            if idx >= n:
                if is_palindrome_partition(seq):
                    partitions.add(tuple(seq))
                return

            seq.append(s[idx])
            backtrack(idx + 1)
            seq.pop()

            if seq:
                seq[-1] = seq[-1] + s[idx]
                backtrack(idx + 1)

        backtrack(0)
        return list(partitions)
