from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        ans = []

        dot_indexes_set = set()
        dot_indexes = []

        def generate_dot_indexes(cur_idx, dot_indexes):
            if cur_idx > n + 1:
                if len(dot_indexes) == 3:
                    dot_indexes_set.add(tuple(dot_indexes))
                return

            dot_indexes.append(cur_idx)
            generate_dot_indexes(cur_idx + 2, dot_indexes)
            dot_indexes.pop()

            generate_dot_indexes(cur_idx + 1, dot_indexes)

        def valid(raw_ip):
            for el in raw_ip:
                if len(el) != len(str(int(el))):
                    return False
                if int(el) > 255:
                    return False
            return True

        generate_dot_indexes(1, dot_indexes)
        for dot_idx_tup in dot_indexes_set:
            a, b, c = dot_idx_tup
            raw_ip = [s[0:a], s[a : b - 1], s[b - 1 : c - 2], s[c - 2 :]]
            if valid(raw_ip):
                ans.append(".".join(raw_ip))

        return ans
