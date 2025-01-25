from typing import List


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        def _topological_sort(adj):
            def _dfs(node):
                if in_stack.get(node, False):
                    return True
                in_stack[node] = True
                for next_node in adj.get(node, []):
                    if in_stack.get(next_node, False):
                        return True
                    if next_node not in visited:
                        _dfs(next_node)

                visited.add(node)
                in_stack[node] = False
                s.append(node)
                return False

            s = []
            visited = set()
            in_stack = {}
            for node in adj:
                if node not in visited:
                    if _dfs(node):
                        return []
            return s[::-1]

        n = len(words)
        adj: dict = {}

        for i, curr_word in enumerate(words):
            next_word = words[i + 1] if i + 1 < n else ""

            is_stop = False
            for j, curr_ch in enumerate(curr_word):
                if curr_ch not in adj:
                    adj[curr_ch] = set()

                if is_stop:
                    continue

                if j < len(next_word) and curr_ch != next_word[j]:
                    adj[curr_ch].add(next_word[j])
                    is_stop = True
                elif j == len(next_word) and i != n - 1:
                    return ""

        ans = _topological_sort(adj)
        return "".join(ans)
