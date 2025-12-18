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

    def max(self, value:int = None):
        if not self.root:
            return None

        if value is None:
            current = self.root
        else:
            current = self.find(value)
        max = current

        print(current.value)

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

        # find the node
        node = self.find(value)
        print(node.value)

        #find max of the node
        predecessor = self.max(node.value)

        return predecessor


    def __str__(self):
        if not self.root:
            return "Empty tree"

        # First, collect all levels
        all_levels = []
        level = [self.root]

        while level:
            current_line = []
            next_level = []

            for node in level:
                if node:
                    current_line.append(str(node.value))
                    next_level.extend([node.left, node.right])
                else:
                    current_line.append("·")
                    next_level.extend([None, None])

            all_levels.append(current_line)
            if any(next_level):
                level = next_level
            else:
                break

        # Calculate spacing
        max_width = len(all_levels[-1]) * 4  # Width based on bottom level
        lines = []

        for i, level_nodes in enumerate(all_levels):
            level_count = 2 ** i
            spacing = max_width // (level_count + 1)
            line = " " * (spacing // 2) + (" " * spacing).join(level_nodes)
            lines.append(line)

        return "\n".join(lines)

tree = Tree()
tree.insert(22)
tree.insert(10)
tree.insert(6)
tree.insert(20)
tree.insert(46)
tree.insert(42)
tree.insert(62)
tree.insert(78)
tree.insert(24)
tree.insert(19)
tree.insert(21)
print(tree)
print(tree.predecessor(10))

# look = tree.find(10)
# print(look.value)
