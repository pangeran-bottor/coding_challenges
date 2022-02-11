class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        pre_sum = [[0]*26]
        for ch in s2:
            new_list = list(pre_sum[-1])
            new_list[ord(ch)-97] += 1
            
            pre_sum.append(new_list)
            
        s1_vec = [0]*26
        for ch in s1:
            s1_vec[ord(ch)-97] += 1
        
        l = len(s1)
        for i in range(l, len(pre_sum)):
            diff_vec = [0] * 26
            for j in range(26):
                diff_vec[j] = pre_sum[i][j] - pre_sum[i-l][j]
            
            is_found = True
            for k in range(26):
                if diff_vec[k] != s1_vec[k]:
                    is_found = False
                    break
            
            if is_found:
                return True
        return False
