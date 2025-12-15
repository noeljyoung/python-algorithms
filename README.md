# Algorithms in Python

1. List
2. Linked List
   1. Linked List fundamentals
      - Insert at beginning O(1)
      - Insert at end O(n)
      - Insert at pos O(n)
      - Delete at beginning O(1)
      - Delete at end O(n)
      - Delete at pos O(n)
      - Searching O(n)
3. Queue
   1. Queue fundamentals
      - A queue follows FIFO: First In → First Out
      - We maintain:
         - head → where we dequeue
         - tail → where we enqueue
      - This gives O(1) operations for both ends.
      - enqueue()
      - dequeue()
      - peek()
      - __len__()
   2. The Correct Real-World Queue: collections.deque
      - from collections import deque
4. Stack
   1. Stack fundamentals
      - A stack is LIFO: Last In, First Out.
      - Core operations:
      - push(x) — add to top
      - pop() — remove and return top
      - peek() — read top without removing
      - is_empty() / __len__()
5. Hash Map
   1. Hash Map fundamentals
      - A hash map (also called a hash table or dictionary) is a data structure that stores key → value pairs and provides:
      - Average O(1) time complexity for:
         - insert
         - lookup
         - delete
      - It achieves this by:
         - Applying a hash function to the key.
         - Converting the hash into an array index.
         - Storing the entry in a bucket at that index.#
      - put(key, value)
      - get(key)
5. Knapsack
    1. Uses dynamic programming to find the optimal solution
