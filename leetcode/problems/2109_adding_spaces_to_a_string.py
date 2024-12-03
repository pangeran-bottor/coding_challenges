from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        chunks = []

        prev = 0
        for idx in spaces:
            chunks.append(s[prev:idx])
            prev = idx
        chunks.append(s[prev:])
        return " ".join(chunks)
