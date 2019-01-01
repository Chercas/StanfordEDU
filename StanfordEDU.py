import numpy as np

M = np.array([[1, 2, 3], 
              [4, 5, 6], 
              [7, 8, 9]])
v = np.array([[1],
              [2],
              [3]])
print(M.shape, '\n')
print(v.shape, '\n')

v_row = np.array([[1, 2, 3]])
print(v_row.shape, '\n')

m = v + v
print(m, '\n')

ones = np.ones((3, 3))
print(type(ones), '\n', ones)
ones_1 = np.full((3, 3), 1)
print(type(ones_1), '\n', ones_1)

v1 = np.array([1, 2, 3])
v2 = np.array([3, 4, 5])
v4 = np.array([5, 6, 7])
v_f = np.stack([v1, v2, v4])
print(v_f.shape, '\n', v_f)