import collections


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        mapper = collections.defaultdict(set)
        n = len(s1)
        for ch1, ch2 in zip(s1, s2):
            mapper[ch1].add(ch2)
            mapper[ch2].add(ch1)

        def collect(ch, visited):
            visited.add(ch)
            if ch not in mapper:
                return visited

            for next_ch in mapper[ch]:
                if next_ch not in visited:
                    visited = visited.union(collect(next_ch, visited))
            return visited

        ans = []
        for ch in baseStr:
            ans.append(min(collect(ch, set())))
        return "".join(ans)
