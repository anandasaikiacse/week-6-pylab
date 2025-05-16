# Q)41) Write a program to demonstrate :
# a) arrays

import numpy as np  
a = np.array(42)  
b = np.array([1, 2, 3, 4, 5])  
c = np.array([[1, 2, 3], [4, 5, 6]])  
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])  
print("entered array is:",a,"and its dimension is:",a.ndim)  
print("entered array is:",b,"and its dimension is:",b.ndim)  
print("entered array is:",c,"and its dimension is:",c.ndim)  
print("entered array is:",d,"and its dimension is:",d.ndim)


# b) array indexing such as slicing, integer array indexing and Boolean array indexing along with their basic operations in NumPy.

import numpy as np  
a=np.arange(10,1,-2)  
print("a sequential array with nagative step value:",a)  
newarr=[a[3],a[1],a[2]]  
print("elements at these indices are:",newarr)  
a=np.arange(20)  
print("Array is:",a)  
print("a[-8:17:1]=",a[-8:17:1])
print("a[10:]=",a[10:])