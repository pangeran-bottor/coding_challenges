class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        idx1, idx2 = 0, 0
        len1, len2 = len(word1), len(word2)
        ans = []
        while idx1 < min(len1, len2) and idx2 < min(len1, len2):
            ans.append(word1[idx1])
            ans.append(word2[idx2])
            idx1 += 1
            idx2 += 1

        for i in range(idx1, len1):
            ans.append(word1[i])
        for j in range(idx2, len2):
            ans.append(word2[j])
        return "".join(ans)
