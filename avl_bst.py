# Guaranteed running time of O(log N)
# The running time of a binary tree depends on the height h of the tree
# in an AVL tree the heights of the two child subtrees of any node differ by at most 1
# ---
# All operations are the same as with BST's
# after every insertion and remove operation we have to check if the tree has become imbalanced or not
# if the tree is imbalanced then we have to make rotations
# ---
# height of a node = max (left child's height + right child's height) + 1
# i.e. the longest path from the node to a leaf node
# ---
# checking the balance factor determines if a tree is imbalanced
# |h(left) - h(right)| > 1
# positive balance factor means left-heavy imbalances
# negative balance factor means right-heavy imbalance
# ---
# Left Rotation:
#   when we have negative balance factor (right heavy) and need to rotate to the left
# Right Rotation:
# when we have postive balance factor (left-heavy) and need to rotate to the right
# after rotation the in-order traversal should remain the same (NB)

class Node:
    def __init__(self, data, parent):
        self.data = data
        self.left_node = None
        self.right_node = None
        self.parent = parent
        self.height = 0 # initialise to 0

class AVLTree:
    def __init(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data, None)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if data < node.data:
            # go left
            if node.left_node is None:
                node.left_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(data, node.left_node)
        elif data > node.data:
            # go right
            if node.right_node is None:
                node.right_node = Node(data, node)
                node.height = max(self.calc_height(node.left_node), self.calc_height(node.right_node)) + 1
            else:
                self.insert_node(data, node.right_node)

        # after every insertion we have to check if the AVL properties are violated
        self.handle_violation(node)

    def remove(self, data):
        if self.root is None:
            pass
        else:
            self.remove_node(data, self.root)

    def remove_node(self, data, node):
        if node is None:
            return

        if data < node.data: # go left
            self.remove_node(data, node.left_node)
        elif data > node.data: # go right
            self.remove_node(data, node.right_node)
        else: # found the node to remove
            # case1: leaf node
            if node.left_node is None and node.right_node is None:
                parent = node.parent

                if parent.left_node == node and parent.right_node is None:
                    parent.left_node = None
                if parent.left_node is None and parent.right_node == node:
                    parent.right_node = None
                if parent is None:
                    self.root = None
                del node

            # case2: one child
            if node.left_node is not None and node.right_node is None:
                node.parent = node.left_node
            elif node.left_node is None and node.right_node is not None:
                node.parent = node.right_node
            # case3: 2 children
            if node.left_node is not None and node.right_node is not None:
                # find predecessor and swap
                self._swap_with_predecessor(node)


    def _find_max(self, node):
        while node.right_node is not None:
            return self._find_max(node.right)

        return node

    def _swap_with_predecessor(self, node):
        predecessor = self._find_max(node.left)
        temp = node
        node = predecessor
        predecessor = temp


    def calc_height(self, node):
        pass

    def handle_violation(self, node):
        pass