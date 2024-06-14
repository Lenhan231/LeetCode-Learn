a = [5,2,1,6,4]
class Node:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

def insert(current,value):
    if value > current.data:
        if current.right is None:
            current.right = Node(value)
        else:
            return insert(current.right, value)
    else:
        if current.left is None:
            current.left = Node(value)
        else:
            return insert(current.left, value)

def in_order_traversal(node):
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end = " ")
        in_order_traversal(node.right)

# Create the root of the tree
root = Node(a[0])

# Insert the rest of the values
for i in range(1, len(a)):
    insert(root, a[i])

# Traverse the tree in order and print the values
in_order_traversal(root)
