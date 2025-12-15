class Tree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None
    
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = self.Node(value)

        if not self.root:
            self.root = new_node
            return

        current = self.root

        while current:
            if new_node.value < current.value: # go left
                if not current.left:
                    current.left = new_node
                else:
                    current = current.left
            elif new_node.value > current.value: # go right
                if not current.right:
                    current.right = new_node
                else:
                    current = current.right

tree = Tree()
tree.insert(10)
print(tree)
