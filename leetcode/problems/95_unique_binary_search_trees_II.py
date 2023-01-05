from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(start, end):
            if start > end:
                return [None]

            all_trees = []
            for i in range(start, end + 1):
                left_trees = generate(start, i - 1)
                right_trees = generate(i + 1, end)

                for l in left_trees:
                    for r in right_trees:
                        current_trees = TreeNode(i)
                        current_trees.left = l
                        current_trees.right = r
                        all_trees.append(current_trees)
            return all_trees

        return generate(1, n)
