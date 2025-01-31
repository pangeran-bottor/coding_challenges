from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def _find(node):
            if representative[node] == node:
                return node
            representative[node] = _find(representative[node])
            return representative[node]

        def _union(node1, node2):
            rep_node1 = _find(node1)
            rep_node2 = _find(node2)
            if size[rep_node1] < size[rep_node2]:
                rep_node1, rep_node2 = rep_node2, rep_node1
            representative[rep_node2] = rep_node1
            size[rep_node1] += size[rep_node2]

        n = len(isConnected)
        representative = [i for i in range(n + 1)]
        size = [1 for i in range(n + 1)]

        ans = n
        for node1 in range(n):
            for node2 in range(node1 + 1, n):
                if isConnected[node1][node2] and _find(node1) != _find(node2):
                    ans -= 1
                    _union(node1, node2)
        return ans
