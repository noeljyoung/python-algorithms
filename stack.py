from node import Node

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def pop(self):
        if not self.top:
            raise IndexError("pop from empty stack")

        value = self.top.value
        self.top = self.top.next
        self.length -= 1
        
        return value
    
    def peek(self):
        if not self.top:
            raise IndexError("peek from empty stack")
        
        return self.top.value
    
    def is_empty(self):
        return self.length == 0
    
    def __len__(self):
        return self.length
    
s = Stack()
s.push(10)
s.push(20)
print(s.peek())   # 20
print(s.pop())    # 20
print(s.pop())    # 10