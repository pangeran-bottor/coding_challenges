class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        letters_dict = {}
        for idx, ch in enumerate(s):
            if ch not in letters_dict:
                letters_dict[ch] = [float("inf"), float("-inf")]

            letters_dict[ch] = [
                min(letters_dict[ch][0], idx),
                max(letters_dict[ch][1], idx),
            ]

        ans = 0
        for letter, (min_idx, max_idx) in letters_dict.items():
            cur_set = set()
            for i in range(min_idx + 1, max_idx):
                cur_set.add(s[i])
            ans += len(cur_set)
        return ans
