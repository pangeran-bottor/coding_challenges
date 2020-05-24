# https://leetcode.com/contest/weekly-contest-190/problems/pseudo-palindromic-paths-in-a-binary-tree/

def pseudo_palindromic_paths(root):
    result = []

    def is_ppal(nodes):
        counter = [0]*10
        for node in nodes:
            counter[node] += 1

        odd_count = 0
        for count in counter:
            if count % 2:
                odd_count += 1
        return odd_count <= 1

    def populate_path(root, path):
        if root is None:
            return
        path.append(root.val)

        if not root.left and not root.right:
            #print(path, is_ppal(path))
            if is_ppal(path):
                result.append(1)

        populate_path(root.left, path)
        populate_path(root.right, path)
        path.pop()

    path = []
    populate_path(root, path)
    return sum(result)
