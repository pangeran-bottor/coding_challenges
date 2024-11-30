from typing import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        count_list = [count for count in counts.values()]
        count_list.sort(reverse=True)

        ans = 0
        found_odd = False
        for count in count_list:
            if count % 2 == 0:
                ans += count
            elif not found_odd:
                ans += count
                found_odd = True
            else:
                ans += count - 1

        return ans
