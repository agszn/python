class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.value, end=" ")
        in_order_traversal(root.right)

def pre_order_traversal(root):
    if root:
        print(root.value, end=" ")
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.value, end=" ")

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal:")
in_order_traversal(root)  # 4 2 5 1 3

print("\nPre-order traversal:")
pre_order_traversal(root)  # 1 2 4 5 3

print("\nPost-order traversal:")
post_order_traversal(root)  # 4 5 2 3 1
