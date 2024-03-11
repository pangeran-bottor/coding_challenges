from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        counts = Counter(s)
        temp = []

        for ch in order:
            temp.append(ch * counts[ch])
            del counts[ch]

        for ch, ct in counts.items():
            temp.append(ch * ct)

        ans = "".join(temp)
        return ans
