class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        pos_map = {}
        ans = 0
        start = 0
        for idx, ch in enumerate(s):
            if ch not in pos_map:
                pos_map[ch] = idx
            else:
                start = max(start, pos_map[ch]+1)
                pos_map[ch] = idx
            ans = max(ans, idx-start+1)
        return ans
