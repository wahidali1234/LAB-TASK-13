class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def kth_smallest(root, k):
    # Helper function for in-order traversal
    def in_order_traversal(node):
        nonlocal count, result

        if node is None or count >= k:
            return

        # Traverse the left subtree
        in_order_traversal(node.left)

        # Process the current node
        count += 1
        if count == k:
            result = node.value
            return

        # Traverse the right subtree
        in_order_traversal(node.right)

    count = 0  # Count of visited nodes
    result = None  # Variable to store the k-th smallest element
    in_order_traversal(root)
    
    return result

# Example usage:
# Construct a sample BST
root = TreeNode(3)
root.left = TreeNode(1)
root.right = TreeNode(4)
root.left.right = TreeNode(2)

k = 2
result = kth_smallest(root, k)
print(f"The {k}-th smallest element is: {result}")
