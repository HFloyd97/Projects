#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# # Using NumPy Arrays

# In[7]:


# Define some vectors
vector_1 = np.array([-2,-6,2,3])
vector_2 = np.array([4,1,-3,8])
vector_3 = np.array([5,-7,9,0])
# Turn our vectors into a matrix
matrix = np.column_stack((vector_1, vector_2, vector_3))

# Print the dimensions of the matrix
print(matrix.shape)


# In[9]:


# View the created matrix
print(matrix)


# In[11]:


# View the 1st column of the matrix
print(matrix[:,0])
# View the 3rd column of the matrix
print(matrix[:,2])


# In[12]:


# View the 1st row of the matrix
print(matrix[0,:])
# View the 3rd row of the matrix
print(matrix[2,:])


# # Using NumPy for Linear Algebra Operations

# In[13]:


# 2 x 3 matrix
A = np.array([[2,3,-4], [-2, 1, -3]])
# 2 x 3 matrix
B = np.array([[1,-1,4], [3,-3,3]])
# 3 x 2 matrix
C = np.array([[1, 2], [3, 4], [5, 6]])


# In[17]:


print(A)
print(B)
print(C)


# In[18]:


# Calculate D = 4A - 2B
D = 4*A - 2*B

# Calculate E = AC
E = A @ C
#E = np.matmul(A,C)

# Calculate F = CA
#F = C @ A
F = np.matmul(C,A)


# # Special Matrices

# In[38]:


A = np.array([[1,-1,1], [0,1,0], [-1,2,1]])
B = np.array([[0.5,1.5,-0.5], [0,1,0], [0.5,-0.5,0.5]])
print(A)
print(B)


# In[36]:


# Multiply matrix A and matrix B 
# Multiply matrix B and matrix A
AB = A@B
BA = B@A

# If AB = BA then the 2 matrices are inverse
print(AB)
print(BA)


# In[39]:


# If a matrix has an inverse we can get the inverse matrix using np.linalg.inv()
A_inverse = np.linalg.inv(A)
print(A_inverse)
# We see that this is equal to B 


# In[22]:


# Get the transposed matrices of A and B
A_transposed = A.T
B_transposed = B.T

print(A_transposed)
print(B_transposed)


# # Additional Linear Algebra Operations

# In[25]:


# Given

#  4x + z = 2
#  -y + 2z - 3x = 0
#  .5y - x - 1.5z = -4

# Solve Ax = b


# In[29]:


# Represent the system in NumPy matrix/vector form. i.e Ax = b
A = np.array([[4,0,1], [-3, -1, 2], [-1, 0.5, - 1.5]])
b = np.array([2, 0, -4])
print(A)
print(b)


# In[31]:


# Solving for x, y, and z
x, y, z = np.linalg.solve(A, b)
print(x, y, z)


# In[34]:


# Get the “norm” (or length/magnitude) of a vector
b_norm = np.linalg.norm(b)
print(b_norm)


# # Example

# In[40]:


# Given

#  2a + 3d - 2c = 4
#  -c + 4b - a = 1
#  2d - 2c + 3a - b = 2
#  -2a + 3c - b = -2

# Solve for a, b, c and d


# In[42]:


# We define A and b
A = np.array([[2, 0,-2, 3], [-1, 4, -1, 0], [3, -1, -2, 2], [-2, -1, 3, 0]])
b = np.array([4, 1, 2, -2])
print(A)
print(b)


# In[43]:


# Solve for a, b, c and d
a, b, c, d = np.linalg.solve(A, b)
print(a, b, c, d)


# In[ ]:




