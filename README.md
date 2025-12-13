# Algorithms in Python

1. Linked List
2. Queue
   1. Queue fundamentals
      - A queue follows FIFO: First In → First Out
      - We maintain:
         - head → where we dequeue
         - tail → where we enqueue
      - This gives O(1) operations for both ends.
   2. The Correct Real-World Queue: collections.deque
      - from collections import deque
3. Stack
   1. Stack fundamentals
      - A stack is LIFO: Last In, First Out.
      - Core operations:
      - push(x) — add to top
      - pop() — remove and return top
      - peek() — read top without removing
      - is_empty() / __len__()
3. Knapsack
    1. Uses dynamic programming to find the optimal solution
