#!/usr/bin/env python3

##
# Binary Search Tree
##


class Node:
    """
    Class that represents a node in the binary search tree.
    Each node contains a value, and pointers to the left and right child nodes.
    """
    def __init__(self, value):
        """
        Initializes a new node with the given value.
        Sets both left and right child pointers to None.
        """
        self.value = value
        self.left = None
        self.right = None

    def display_node(self):
        """
        Prints the value of the current node.
        """
        print(self.value)


class BinarySearchTree:
    """
    Class that represents a Binary Search Tree (BST).
    Supports operations like insert, search, delete, and tree traversal.
    """
    def __init__(self):
        """
        Initializes an empty binary search tree with no root.
        """
        self.root = None

    def insert(self, value):
        """
        Inserts a value into the binary search tree.
        The value is placed in the correct position based on BST properties.
        """
        new_node = Node(value)
        
        # If the tree is empty
        if self.root is None:
            self.root = new_node
        else:
            current = self.root
            while True:
                parent = current
                # Left
                if value < current.value:
                    current = current.left
                    if current is None:
                        parent.left = new_node
                        return
                # Right
                else:
                    current = current.right
                    if current is None:
                        parent.right = new_node
                        return

    def search(self, value):
        """
        Searches for a value in the binary search tree.
        Returns the node containing the value if found, otherwise returns None.
        """
        current = self.root
        while current and current.value != value:
            if value < current.value:
                current = current.left
            else:
                current = current.right
        return current

    def pre_order(self, node):
        """
        Traverses the tree in pre-order: root, left, right.
        Prints the value of each node.
        """
        if node:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def in_order(self, node):
        """
        Traverses the tree in in-order: left, root, right.
        Prints the value of each node.
        """
        if node:
            self.in_order(node.left)
            print(node.value)
            self.in_order(node.right)

    def post_order(self, node):
        """
        Traverses the tree in post-order: left, right, root.
        Prints the value of each node.
        """
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.value)

    def delete(self, value):
        """
        Deletes a node with the specified value from the tree.
        Handles all cases: no children, one child, and two children.
        """
        if self.root is None:
            print("The tree is empty.")
            return False

        # Find the node to delete
        current = self.root
        parent = self.root
        is_left_child = True
        while current and current.value != value:
            parent = current
            if value < current.value:
                is_left_child = True
                current = current.left
            else:
                is_left_child = False
                current = current.right
            if current is None:
                return False

        # Case 1: Node to be deleted has no children (leaf node)
        if current.left is None and current.right is None:
            if current == self.root:
                self.root = None
            elif is_left_child:
                parent.left = None
            else:
                parent.right = None

        # Case 2: Node to be deleted has no right child
        elif current.right is None:
            if current == self.root:
                self.root = current.left
            elif is_left_child:
                parent.left = current.left
            else:
                parent.right = current.left

        # Case 3: Node to be deleted has no left child
        elif current.left is None:
            if current == self.root:
                self.root = current.right
            elif is_left_child:
                parent.left = current.right
            else:
                parent.right = current.right

        # Case 4: Node to be deleted has two children
        else:
            successor = self.get_successor(current)
            if current == self.root:
                self.root = successor
            elif is_left_child:
                parent.left = successor
            else:
                parent.right = successor
            successor.left = current.left

        return True

    def get_successor(self, node):
        """
        Gets the in-order successor of a given node.
        The in-order successor is the smallest node in the right subtree.
        """
        parent_successor = node
        successor = node
        current = node.right
        while current:
            parent_successor = successor
            successor = current
            current = current.left

        if successor != node.right:
            parent_successor.left = successor.right
            successor.right = node.right
        return successor


# Test the Binary Search Tree
tree = BinarySearchTree()
tree.insert(53)
tree.insert(30)
tree.insert(14)
tree.insert(39)
tree.insert(9)
tree.insert(23)
tree.insert(34)
tree.insert(49)
tree.insert(72)
tree.insert(61)
tree.insert(84)
tree.insert(79)

# Search operations
found_node_1 = tree.search(39)
if found_node_1:
    print(f"Node with value {found_node_1.value} found.")
else:
    print("Node with value 39 not found.")

found_node_2 = tree.search(84)
if found_node_2:
    print(f"Node with value {found_node_2.value} found.")
else:
    print("Node with value 84 not found.")

found_node_3 = tree.search(100)
if found_node_3:
    print(f"Node with value {found_node_3.value} found.")
else:
    print("Node with value 100 not found.")

# Deletion operations
tree.delete(9)
tree.delete(14)
tree.delete(72)

# Traverse the tree in order
print("\nIn-order traversal:")
tree.in_order(tree.root)

# Traverse the tree in pre-order
print("\nPre-order traversal:")
tree.pre_order(tree.root)

# Traverse the tree in post-order
print("\nPost-order traversal:")
tree.post_order(tree.root)
