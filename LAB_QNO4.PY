class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_path(root, node, path):
    if root is None:
        return False

    path.append(root)

    if root == node:
        return True

    if (root.left and find_path(root.left, node, path)) or (root.right and find_path(root.right, node, path)):
        return True

    path.pop()
    return False

def find_lca(root, node1, node2):
    path1 = []
    path2 = []

    if not find_path(root, node1, path1) or not find_path(root, node2, path2):
        return None

    lca = None
    for i in range(min(len(path1), len(path2))):
        if path1[i] == path2[i]:
            lca = path1[i]
        else:
            break

    return lca

# Example usage:
# Construct a simple binary tree
