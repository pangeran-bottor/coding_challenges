from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        counts = [(ch, count) for ch, count in Counter(s).items()]
        counts.sort(key=lambda x: -x[1])

        sorted_chars = []
        for ch, count in counts:
            for i in range(count):
                sorted_chars.append(ch)
        
        return "".join(sorted_chars)
