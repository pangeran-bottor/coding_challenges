class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        uppercase = 0
        for ch in word:
            if ch.isupper():
                uppercase += 1

        if uppercase == len(word):
            return True
        
        if uppercase == 1 and word[0].isupper():
            return True

        return uppercase == 0
