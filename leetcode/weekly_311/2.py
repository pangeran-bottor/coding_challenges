class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        ans = 0
        set_list = []
        for ch in s:
            if len(set_list) == 0:
                set_list.append([ch])
            else:
                if ord(ch) - ord(set_list[-1][-1]) == 1:
                    set_list[-1].append(ch)
                else:
                    set_list.append([ch])
        for l in set_list:
            ans = max(ans, len(l))
        return ans
