class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        key_map = {}
        for idx, ch in enumerate(keyboard):
            key_map[ch] = idx

        start_idx = 0
        ans = 0
        for ch in word:
            cur_idx = key_map[ch]
            ans += abs(cur_idx - start_idx)
            start_idx = cur_idx
        return ans
