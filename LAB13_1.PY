class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def height_of_binary_tree(root):
    if root is None:
        return -1
    else:
        left_height = height_of_binary_tree(root.left)
        right_height = height_of_binary_tree(root.right)
        return 1 + max(left_height, right_height)

# Example usage:
# Assuming you have a binary tree with nodes, and 'root' is the reference to the root node.
# height = height_of_binary_tree(root)
