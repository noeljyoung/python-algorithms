from collections import namedtuple
from typing import List, Tuple

Item = namedtuple("Item", ["index", "value", "weight"])

items = [Item(1, 16, 2), Item(2, 19, 3), Item(3, 23, 4), Item(3, 28, 5)]
# items.sort(key=lambda item: item.weight, reverse=True)

print(items[0])
print(items[1])
print(items[2])

memo = {}


def o(k: int, j: int):
    """Objective function with k=capacity, j=item number in the list"""
    if j < 0:
        return 0

    if (k, j) in memo:
        return memo[(k, j)]

    if items[j].weight <= k:
        item_weight = items[j].weight
        item_value = items[j].value
        # item fits check if this item or
        memo[(k,j)] = max( o(k, j-1), item_value + o(k - item_weight, j-1) )
    else:
        memo[(k,j)] = o(k, j-1) # item does not fit, skip to next item

    return memo[(k,j)]

K = 7 # capacity of the knapsack
matrix = [[0 for _ in range(K + 1)] for _ in range(len(items))]
max_value = 0

for item in range(len(items)):
    for capacity in range(0, K + 1):
        matrix[item][capacity] = o(capacity, item)
        max_value = max(max_value, o(capacity, item))

# for item in items:
#     print(item)

print(max_value)

for row in matrix:
    print(row)

print(memo)