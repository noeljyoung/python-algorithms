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
print('done')
