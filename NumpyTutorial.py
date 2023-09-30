import numpy as np
import time
import sys

if __name__ == '__main__':
    # l = range(1000)  # making a list which size is 1000
    # print(sys.getsizeof(1) * len(l))
    #
    # ara = np.arange(1000)  # making a array of 1000 length,arange = range for list
    # print(ara.size * ara.itemsize)
    # ara.size = total length of array
    # ara.itemize = size of one item
    # numpy array will be lower in size than traditional python array

    # proving why numpy array are faster than python list
    # sz = 100000
    #
    # l1 = range(sz)
    # l2 = range(sz)
    #
    # a1 = np.arange(sz)
    # a2 = np.arange(sz)
    #
    # # checking time for computing python list
    # start = time.time()
    # res = [(x + y) for x, y in zip(l1, l2)]
    # # takes one item from l1 and one item from l2 and adds them and stores them in res list
    # print("Python list took = ", (time.time() - start) * 1000)
    #
    # # checking time for computing numpy array
    # start = time.time()
    # res = a1 + a2  # does same as above list comprehension
    # print("numpy array took = ", (time.time() - start) * 1000)

    # after executing the program -
    # Python list took = 15.7470703125
    # numpy array took = 4.986047744750977

    # video 2 - basic array operations
    # a = np.array([5,6,9])
    # print(a[0])

    # ndim
    # a = np.array([[1, 2], [3, 4], [5, 6]])
    # print(a.ndim)

    # #itemsize
    # print(a.itemsize) #outputs 8 . size of one item , it is showing 8 for compile, int size is generally 4bytes
    #
    # #data type of current array
    # print(a.dtype) #output int64

    # if we want to change the data type of the array
    #
    # a = np.array([[1, 2], [3, 4], [4, 5]], dtype=np.float64)
    # # print(a.dtype)#now the array becomes of float data type
    # print(a.itemsize)

    # SIZE
    # print(a.size)  # total number of elements
    #
    # # shape
    # print(a.shape) # return how many rows and column the array has
    # print(a)

    # a = np.array([[1,2],[3,4],[4,5]],dtype=complex)
    # print(a)
    # [ [1. + 0.j 2. + 0.j]
    #   [3. + 0.j 4. + 0.j]
    #   [4. + 0.j 5. + 0.j] ]

    # if you want to initialize array with placeholder value
    # a = np.zeros((3, 4))  # in zeros function pass the dimension of your desired matrix
    # print(a)
    # b = np.ones((5, 4))  # in ones function pass the dimension of your desired matrix
    # print(b)

    # arange

    # makes a 1d array of 1 to 14
    # a = np.arange(1, 15)  # [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14]
    # print(a)
    # if you want to make the items 1,3,5..
    # a = np.arange(1, 20, 2)
    # print(a)  # [ 1  3  5  7  9 11 13 15 17 19]

    # linspace
    # a = np.linspace(1,5,10)
    # print(a)
    # a = np.linspace(1, 5, 100)
    # print(a)

    # reshape
    #
    # a = np.array([[1, 2], [3, 4], [5, 6]])
    # print("Before operation")
    # print(a)
    # print(f"Shape = {a.shape}")
    # print("After operation")
    # b = a.reshape(2, 3)  # .reshape returns a new array, rather than reshaping in place.
    # print(b)
    # print(f"Shape = {b.shape}")

    # ravel ( makes the array one dimensional)
    # a = np.array([[1, 2], [3, 4], [5, 6]])
    # print("Before using ravel")
    # print(a)
    # print("After using ravel")
    # b = a.ravel()
    # print(b)

    # mathematical functions

    # a = np.array([[1, 2, 3, 0, 1], [3, 4, 9, 4, 2], [4, 5, 1, 2, 3], [6, 10, 11, 12, 11]])
    # print(a.min())
    # print(a.max())
    # print(a.sum())
    # axis = 0 (column wise)        # axis = 1 (row wise)
    # axis wise operation returns list object, so to use those returned values you can use another
    # list to store the return values
    # # row wise
    # print("Row wise operations")
    # print(a.min(axis=1))  # shows minimum values of each row
    # print(a.max(axis=1))  # shows max values of each row
    # print(a.sum(axis=1))  # shows sum of values of each row
    # b = a.sum(axis=1) # storing the values in  a list
    # print(b)
    # # column wise
    # print("Row wise operations")
    # print(a.min(axis=0))  # shows minimum values of each column
    # print(a.max(axis=0))  # shows max values of each column
    # print(a.sum(axis=0))  # shows sum of values of each column
    #
    # # you can not use sqrt function directly with array object -> a, you have to use numpy keyword
    #
    # print(np.sqrt(a))  # sqrt of each element in the matrix
    #
    # # standard deviation
    # print(np.std(a))

    # matrix operations
    #
    # a = np.array([[1,2],[3,4],[5,6],[4,1]])
    # b = np.array([[2,3],[4,5],[6,1],[4,3]])
    # print(a+b)
    # print(a-b)
    # print(a*b)
    # print(a/b)
    # print(a.dot(b))# dot product
    #
    # video 3 slicing/stacking arrays, indexing with boolean arrays

    # slicing in list
    # li = [1, 3, 4, 4, 1, 3, 4]
    # print(li[0:4])

    # slicing in 1D array
    # a = np.array([1, 2, 3, 4, 5, 6, 8])
    # print(a[0:4])

    # Modify Array Elements Using Slicing

    # a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # a[3:] = 40
    # print(a)  # [ 1  2  3 40 40 40 40 40 40 40] #the array is filled with 40 from index 3
    # b1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # b1[:3] = 31  # [31 31 31  4  5  6  7  8  9 10] #the array is filled with 31 from 0 until index 3
    # print(b1)
    #
    # c1 = np.array([1, 2, 3, 4, 5, 6, 7])
    # c1[2:4] = 100  # [  1   2 100 100   5   6   7]
    # print(c1)
    #
    # d1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    # d1[1:6:2] = 20  # From index 1 until 6 jump by 2 and make the item = 20
    # print(d1)  # [ 1 20  3 20  5 20  7  8  9 10]

    # 2D NumPy Array Slicing
    # array[row_start:row_stop:row_step, col_start:col_stop:col_step]

    # a1 = np.array([[1,3,5,7],
    #                [9,11,13,15]])
    #
    # print(a1[:2,:2])

    # a1 = np.array([[1,2,3],
    #                [4,3,2],
    #                [6,5,4]])

    # slice the array to get the first two rows and columns
    # print(a1[:2,:2])
    # a1[:2, :2] - slices a1 array that starts at the first row and first column (default values),
    # and ends at the second row and second column (exclusive)
    # [[1 2]
     # [4 3]]
    # slice the array to get the last two rows and columns
    # print(a1[1:3,1:3])
    # [[3 2]
     # [5 4]]




