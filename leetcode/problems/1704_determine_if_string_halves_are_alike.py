class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = "aiueoAIUEO"
        n = len(s)
        mid = (n-1)//2
        
        count = 0
        for i in range(mid+1):
            if s[i] in vowels:
                count += 1

        for i in range(mid+1, n):
            if s[i] in vowels:
                count -= 1

        return count == 0
