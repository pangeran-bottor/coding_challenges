class Solution:
    def partitionString(self, s: str) -> int:
        splitted = [set()]
        
        
        for ch in s:
            if ch not in splitted[-1]:
                splitted[-1].add(ch)
            else:
                splitted.append(set())
                splitted[-1].add(ch)
        return len(splitted)
