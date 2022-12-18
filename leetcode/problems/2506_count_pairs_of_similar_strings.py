from collections import Counter
from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        def encode(word):
            encoded = [0 for _ in range(26)]
            for ch in word:
                encoded[ord(ch)-97] = 1
            return "".join(map(str, encoded))

        ans = 0
        encoded_map = Counter()
        for word in words:
            encoded = encode(word)
            encoded_map[encoded] += 1

        for count in encoded_map.values():
            ans += (count*(count-1))//2
        return ans
