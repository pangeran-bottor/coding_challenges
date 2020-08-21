class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def is_valid(cur_dict, target_dict):
            for k, v in target_dict.items():
                if cur_dict.get(k, 0) < v:
                    return False
            return True

        ans = ""
        cur_dict = {}
        target_dict = {}
        for ch in t:
            if ch not in target_dict:
                target_dict[ch] = 0
            target_dict[ch] += 1
        
        i, j = 0, 0
        while j < len(s):
            if s[j] not in cur_dict:
                cur_dict[s[j]] = 0
            cur_dict[s[j]] += 1

            while is_valid(cur_dict, target_dict):
                if not ans or j+1-i < len(ans):
                    ans = s[i:j+1]
                
                cur_dict[s[i]] -= 1
                i += 1
            
            j += 1
        
        return ans
