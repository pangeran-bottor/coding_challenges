class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ans = -1

        n_haystack = len(haystack)
        n_needle = len(needle)
        for i in range(n_haystack - n_needle + 1):
            found = True
            for j in range(n_needle):
                if i + j >= n_haystack:
                    return ans

                if haystack[i + j] != needle[j]:
                    found = False
            if found:
                return i
        return ans
