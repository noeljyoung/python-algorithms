class BinarySearchTree:
    class Node:
        def __init__(self, data, parent=None):
            self.data = data
            self.left = None
            self.right = None
            self.parent = parent

    def __init__(self):
        self.root = None

    def insert(self, data):
        new_node = self.Node(data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert_node(data, self.root)

    def remove(self, data):
        if self.root:
            self._remove_node(data, self.root)

    def _insert_node(self, data, node):
        if data < node.data:
            # go left
            if node.left is None:
                node.left = self.Node(data, node)
            else:
                self._insert_node(data, node.left)
        elif data > node.data:
            # go right
            if node.right is None:
                node.right = self.Node(data, node)
            else:
                self._insert_node(data, node.right)

    def _remove_node(self, data, node):
        # find the node we want to remove
        if node is None:
            return

        if data < node.data:
            self._remove_node(data, node.left)
        elif data > node.data:
            self._remove_node(data, node.right)
        else:
            # remove the node using the 3 options:
            # NODE IS A LEAF
            if node.left is None and node.right is None:
                print("Removing a leaf node %d" % node.data)
                parent = node.parent

                if parent is not None and parent.left == node:
                    # our node is the left child of its parent
                    parent.left = None

                if parent is not None and parent.right == node:
                    # our node is the right child of its parent
                    parent.right = None

                if parent is None:
                    # we are deleting the root node which has no children
                    self.root = None

                del node # clean up the deleted node
            # NODE HAS 1 CHILD
            elif node.left is not None and node.right is None:
                print("Removing a node with single left child %d" % node.data)
                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = node.left

                if parent is not None and parent.right == node:
                    parent.right = node.left

                if parent is None:
                    self.root = node.left

                node.left.parent = parent

                del node
            elif node.left is None and node.right is not None:
                print("Removing a node with single right child %d" % node.data)
                parent = node.parent

                if parent is not None and parent.left == node:
                    parent.left = node.right

                if parent is not None and parent.right == node:
                    parent.right = node.right

                if parent is None:
                    self.root = node.right

                node.right.parent = parent

                del node

            # node has 2 children
            else:
                print("Removing a node with 2 children %d" % node.data)
                # predecessor is the maximum value of the node's left side
                predecessor = self._get_predecessor(node.left)

                # swap the node and predecessor
                print(f"Swapping {predecessor.data} and {node.data}")

                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp

                self._remove_node(data, predecessor)

                del node


    def _get_predecessor(self, node):
        if node.right:
            self._get_predecessor(node.right)

        return node

    def get_min(self):
        if self.root:
            return self._get_min_value(self.root)

    def _get_min_value(self, node):
        if node.left:
            return self._get_min_value(node.left)

        return node.data

    def get_max(self):
        if self.root:
            return self._get_max_value(self.root)

    def _get_max_value(self, node):
        if node.right:
            return self._get_max_value(node.right)

        return node.data

    def traverse_in_order(self, node=None):
        if node is None:
            node = self.root

        if node.left:
            self.traverse_in_order(node.left)

        print(node.data)

        if node.right:
            self.traverse_in_order(node.right)

    # def levelOrderRec(root, level, res):
    #     # Base case
    #     if root is None:
    #         return

    #     # Add a new level to the result if needed
    #     if len(res) <= level:
    #         res.append([])

    #     # Add current node's data to its corresponding level
    #     res[level].append(root.data)

    #     # Recur for left and right children
    #     level_order_rec(root.left, level + 1, res)
    #     level_order_rec(root.right, level + 1, res)

    # # Function to perform level order traversal
    # def levelOrder(root):
    #     # Stores the result level by level
    #     res = []
    #     level_order_rec(root, 0, res)
    #     return res


bst = BinarySearchTree()
bst.insert(10)
bst.insert(4)
bst.insert(12)
bst.insert(1)
bst.insert(2)
bst.insert(-2)
bst.insert(200)
bst.insert(24)
min = bst.get_min()
max = bst.get_max()
print('min: ' + str(min))
print('max: ' + str(max))
bst.traverse_in_order()
print("---")
bst.remove(10)
bst.remove(4)
bst.remove(12)
bst.remove(1)
bst.remove(2)
bst.remove(-2)
bst.remove(200)
bst.remove(24)
print("->")
bst.traverse_in_order()
print('done')
