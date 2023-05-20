import numpy as np

# numpy array
np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
print(type(np_array))

# Creating a 1 dimensional numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)

# shape function - It tells us the rows and columns in that particular array
print(a.shape)

# Creating a 2-dimensional numpy array
print("2-Dimensional numpy array")
b = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(b)
print(b.shape)

# Initial placeholders in numpy array
x = np.zeros((4, 5))
print(x)

y = np.ones((5, 5))
print(y)

z = np.full((3, 3), 5)
print(z)

# Identity matrix
print('\nIdentity Matrix')
i = np.eye(5)
print(i)

# Creating numpy array with random values between 0 & 1
print('\nNumpy array with random values')
r = np.random.random((3, 3))
print(r)

# Creating numpy array with random values with random integers
random_int_array = np.random.randint(10, 100, (5, 5))
print(random_int_array)

# array of evenly spaced values
print('\nArray of evenly spaced values')
d = np.linspace(10, 30, 5)
print(d)

# array of evenly spaced values --> specifying the step
print('\nArray of evenly spaced values with specific step')
e = np.arange(10, 30, 5)
print(e)

print()

# Converting a list to numpy array
list2 = [1, 2, 3, 4, 5]
list_to_array = np.asarray(list2)

print(list2, type(list2))
print(list_to_array, type(list_to_array))

# Analysing a numpy array
np_array2 = list_to_array

print(np_array2.shape)
print(np_array2.size)
print(np_array2.ndim)

# checking the data type of values in the array
print(np_array2.dtype)

# Mathematical operations on the numpy array
list3 = [1, 2, 3, 4, 5]
list4 = [6, 7, 8, 9, 10]

print(list3 + list4)  # concatenate the lists

np_list3 = np.array(list3)
np_list4 = np.array(list4)

print(np_list3 + np_list4)
print(np_list3 - np_list4)
print(np_list3 * np_list4)
print(np_list3 / np_list4)

print(np.transpose(np_list3))