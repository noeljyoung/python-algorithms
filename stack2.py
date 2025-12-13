from node import Node

class Stack:
    def __init__(self):
        self._items = [] # Typically we would use a List implementation

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if not self._items:
            raise IndexError("pop from empty stack")
        
        return self._items.pop()
    
    def peek(self):
        if not self._items:
            raise IndexError("peek from empty stack")
        
        return self._items[-1] # return last item in the List
    
    def is_empty(self):
        return len(self._items) == 0

    def __len__(self):
        return len(self._items)
    
s = Stack()
s.push("a")
s.push("b")
print(s.pop())  # "b"