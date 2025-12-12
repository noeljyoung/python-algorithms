class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def prepend(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        self.head = new_node
        self.head.next = current

    def find(self, value):
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None


    def __iter__(self):
        current = self.head
        while current:
            yield current.value # return the value
            current = current.next # move pointer to next node

    def __len__(self):
        count = 0
        for x in self.__iter__():
            count += 1

        return count


ll = LinkedList()

ll.append(20)
ll.append(10)
ll.append(30)
ll.append(40)
ll.append(70)
ll.prepend(4)
ll.prepend(43)

print(list(ll))
print (len(ll))

fll = ll.find(3)
print(fll)
