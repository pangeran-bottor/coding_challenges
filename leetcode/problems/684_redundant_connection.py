from typing import List


class UnionFind:
    def __init__(self, N):
        self.representative = [i for i in range(N + 1)]
        self.size = [1 for _ in range(N + 1)]

    def find(self, node):
        if self.representative[node] == node:
            return node
        self.representative[node] = self.find(self.representative[node])
        return self.representative[node]

    def union(self, node1, node2):
        rep_node1 = self.find(node1)
        rep_node2 = self.find(node2)
        if rep_node1 == rep_node2:
            return False

        if self.size[rep_node1] < self.size[rep_node2]:
            rep_node1, rep_node2 = rep_node2, rep_node1
        self.representative[rep_node2] = rep_node1
        self.size[rep_node1] += self.size[rep_node2]
        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        union_find = UnionFind(len(edges) + 1)
        for node1, node2 in edges:
            if not union_find.union(node1, node2):
                return [node1, node2]
        return []
