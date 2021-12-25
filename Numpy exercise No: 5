

"""
 Questions:
write a Numpy program to extract upper triangular part of a Numpy Matrix. 

write a Numpy Program to extract all the elements of the second and third columns from a given (4x4) my_array.

write a Numpy program to count the occurrence of a specified item in a given Numpy my_array.

write anumpy program to sum and compute the product of a Numpy my_array elements.

"""

import numpy as np

mat1 = np.array([[1,2,3,4], [5,6,7,8], [8,9,10,11]])
print('The shape of mat is:', mat1.shape)
# it can be reshaped to any shape that is consistent with the data size
new_mat1 = mat1.reshape(1,12)
print('The shape of new_mat1 is:', new_mat1.shape)
# you can try transposing it as well.
trans_new_mat1 = new_mat1.T
print('The transposed shape of new_mat1 is:', trans_new_mat1.shape)

# write a Numpy program to extract upper triangular part of a Numpy Matrix.
mat1[np.triu_indices(3)]

# write a Numpy Program to extract all the elements of the second and third columns from a given (4x4) my_array.
print(mat1[:,[1,2]])

# write a Numpy program to count the occurrence of a specified item in a given Numpy my_array.
len(mat1)

# write anumpy program to sum and compute the product of a Numpy my_array elements.

print(mat1.sum())


###################################### output ###################################################################


mat1 = np.array([[1,2,3,4], [5,6,7,8], [8,9,10,11]])

new_mat1 = mat1.reshape(1,12)

new_mat1
Out[5]: array([[ 1,  2,  3,  4,  5,  6,  7,  8,  8,  9, 10, 11]])

trans_new_mat1 = new_mat1.T

trans_new_mat1
Out[7]: 
array([[ 1],
       [ 2],
       [ 3],
       [ 4],
       [ 5],
       [ 6],
       [ 7],
       [ 8],
       [ 8],
       [ 9],
       [10],
       [11]])

mat1[np.triu_indices(3)]
Out[8]: array([ 1,  2,  3,  6,  7, 10])

print(mat1[:,[1,2]])
[[ 2  3]
 [ 6  7]
 [ 9 10]]

len(mat1)
Out[10]: 3

print(mat1.sum())
74

