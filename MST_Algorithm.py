import numpy as np
from scipy.sparse.csgraph import minimum_spanning_tree as mst

d = np.array([
    [0, 10, 6, 5, 0],
    [10, 0, 0, 15, 4],
    [6, 0, 0, 4, 3],
    [5, 6, 4, 0, 0],
    [0, 4, 3, 0, 0],
])

tree = mst(d)
print(tree)

# cost = 0
# for tree in
# cost += tree
# print(cost)

'''
[0, 8, 0, 3],
    [8, 0, 2, 5],
    [0, 2, 0, 6],
    [3, 5, 6, 0]
'''