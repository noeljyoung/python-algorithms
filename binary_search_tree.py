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
                    return
                else:
                    current = current.left
            elif new_node.value > current.value: # go right
                if not current.right:
                    current.right = new_node
                    return
                else:
                    current = current.right
            elif new_node.value == current.value:
                return;

    def find(self, value):
        if not self.root:
            return None

        current = self.root

        while current:
            leaf = current
            if value == current.value: # value is found
                break
            elif value < current.value: # go left
                current = current.left
            elif value > current.value: # go right
                current = current.right

        return leaf

    def max(self):
        if not self.root:
            return None

        current = self.root
        max = current

        while current:
            if current.right is not None:
                max = current.right

            current = current.right

        return max.value

    def min(self):
        if not self.root:
            return None

        current = self.root
        min = current

        while current:
            if current.left is not None:
                min = current.left
            current = current.left

        return min.value

    def predecessor(self, value):
        if self.root is None:
            return None

        current = self.root


    def __str__(self):
        if not self.root:
            return "Empty tree"

        lines = []
        level = [self.root]

        while level:
            current_line = []
            next_level = []

            for node in level:
                if node:
                    next_level.extend([node.left, node.right])
                else:
                    current_line.append("·")
                    next_level.extend([None, None])

            if any(next_level):
                lines.append(" ".join(current_line))
                level = next_level
            else:
                lines.append(" ".join(current_line))
                break

        return "\n".join(lines)

tree = Tree()
tree.insert(10)
tree.insert(19)
tree.insert(11)
tree.insert(9)
tree.insert(1)
tree.insert(10)
# print(tree)
print(tree.min())
print(tree.max())

# look = tree.find(10)
# print(look.value)
