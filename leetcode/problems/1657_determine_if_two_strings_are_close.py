from collections import Counter


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        counts1, counts2 = Counter(word1), Counter(word2)

        countmap1 = Counter(count for count in counts1.values())
        countmap2 = Counter(count for count in counts2.values())
        return countmap1 == countmap2 and set(word1) == set(word2)
