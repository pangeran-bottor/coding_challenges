class Solution:
    def countValidWords(self, sentence: str) -> int:
        def _is_valid_contains(word):
            for ch in word:
                if not ch.islower() and ch not in "!,.-":
                    return False
            return True

        def _is_valid_hyphen(word):
            count = 0
            for idx, ch in enumerate(word):
                if ch == "-":
                    count += 1
                    if count > 1:
                        return False
                    if idx == 0 or idx == len(word) - 1:
                        return False
                    if not word[idx - 1].islower() or not word[idx + 1].islower():
                        return False
            return True

        def _is_valid_punc(word):
            count = 0
            for idx, ch in enumerate(word):
                if ch in "!,.":
                    count += 1
                    if count > 1:
                        return False
                    if idx != len(word) - 1:
                        return False
            return True

        ans = 0
        for raw_word in sentence.split():
            word = raw_word.strip()
            if not _is_valid_contains(word):
                continue
            # print("valid contains")
            if not _is_valid_hyphen(word):
                continue
            # print("valid hyphen")
            if not _is_valid_punc(word):
                continue
            # print("valid punc")

            ans += 1
        return ans
