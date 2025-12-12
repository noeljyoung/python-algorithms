from node import Node

class Queue:
    def __init__(self):
        self.head = None # dequeue from here
        self.tail = None # enqueue from here
        self.length = 0

    def enqueue(self, value):
        """Add item to the back of the queue"""
        new_node = Node(value)

        if not self.tail: #empty queue
            self.tail = new_node
            self.head = new_node
        else:
            self.tail.next = new_node # point the current tail node to the new enqueued node
            self.tail = new_node # update our queue tail to point to the new node

        self.length += 1

    def dequeue(self):
        """Remove item from the front of the queue"""
        if not self.head:
            raise IndexError("dequeue from empty queue")

        value = self.head.value
        self.head = self.head.next

        if self.head is None: # queue is now empty
            self.tail = None

        self.length -= 1

        return value

    def peek(self):
        """Return the item at the front without removing it"""
        if not self.head:
            raise IndexError("peek from empty queue")

        return self.head.value

    def __len__(self):
        return self.length


q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)

print('current next item: ' + str(q.peek()))

next_item = q.dequeue()
print('dequeued item: ' + str(next_item))

print('new next item: ' + str(q.peek()))