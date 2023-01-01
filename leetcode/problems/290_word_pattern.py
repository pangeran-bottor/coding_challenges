class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word_map = {}
        ch_set = set()

        s_list = s.split()
        if len(pattern) != len(s_list):
            return False

        for ch, word in zip(pattern, s_list):
            if word not in word_map:
                if ch not in ch_set:
                    word_map[word] = ch
                    ch_set.add(ch)
                else:
                    return False
            else:
                if word_map[word] != ch:
                    return False
        return True
