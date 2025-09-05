# import numpy as np
# Q1
# arr1D=np.arange(5,26)
# print("1D Array from 5 to 25:\n",arr1D)

# arr2D=np.random.randint(10,51, size=(3,4))
# print("\n2D Array (3x4) with random integers between 10 and 50:\n",arr2D)


# Q2
# arr1D=np.arange(5,26)
# print("1D Array from 5 to 25:\n",arr1D)
# print("Shape:\n",arr1D.shape)
# print("Size:\n",arr1D.size)
# print("Data type:\n",arr1D.dtype)

# arr2D=np.random.randint(10,51, size=(3,4))
# print("\n2D Array (3x4) with random integers between 10 and 50:\n",arr2D)
# print("Shape:\n",arr2D.shape)
# print("Size:\n",arr2D.size)
# print("Data type:\n",arr2D.dtype)


# Q3
# list1=[2,4,6,8,10]
# list2=[1,3,5,7,9]
# arr1=np.array(list1)
# arr2=np.array(list2)
# print(arr1,"\n",arr2)

# print("Addition:", arr1 + arr2)
# print("Subtraction:", arr1 - arr2)
# print("Element-wise Multiplication:", arr1 * arr2)
# print("Element-wise Division:", arr1 / arr2)


# Q4
# arr=np.arange(1,10).reshape(3,3)
# print("2D Array (3x3):\n",arr)

# result=arr*5
# print("Broadcasted Array (multiplied by 5):\n",result)


# Q5
# arr=np.arange(10,26).reshape(4,4)
# print(arr)

# second_row=arr[1,:]
# last_column=arr[:,-1]
# print("\nSecond Row:", second_row)
# print("Last Column:", last_column)

# arr[0,:]=0
# print("First row replaced with zeros\n",arr)


# Q6
# arr=np.random.randint(20,41,size=10)
# print("Random 1D Array (10 elements between 20 and 40):\n",arr)

# boo=arr>30
# print("Elements greater than 30:\n", boo)


# Q7
# arr=np.arange(11,23)
# print("1D Array with 12 elements starting from 11:\n", arr)

# reshaped_arr=arr.reshape(3,4)
# print("Reshaped array:\n",reshaped_arr)


# Q8
# matrixA = np.array([[1, 2], [3, 4]])
# matrixB = np.array([[5, 6], [7, 8]])
# print(matrixA,"\n",matrixB)

# matrix_multiplication = np.dot(matrixA, matrixB)
# transpose_A = matrixA.T
# print("\nMatrix Multiplication of A and B:\n", matrix_multiplication)
# print("Transpose of Matrix A:\n", transpose_A)


# Q9
# arr=np.random.randint(10,61,size=15)
# print(arr)

# print("Mean:",np.mean(arr))
# print("Median:",np.median(arr))
# print("Standard Deviation:",np.std(arr))


# Q10
# A=np.array([[2,1,3],
#           [0,5,6],
#         [7,8,9]])
# print(A)

# det_A = np.linalg.det(A)
# print("\nDeterminant of A:", det_A)

# try:
#     inv_A = np.linalg.inv(A)
#     print("\nInverse of A:\n", inv_A)
# except np.linalg.LinAlgError:
#     print("\nMatrix A is singular and cannot be inverted.")

# eigenvalues, eigenvectors = np.linalg.eig(A)
# print("\nEigenvalues of A:\n", eigenvalues)
# print("\nEigenvectors of A:\n", eigenvectors)


# Q11
# positions = np.array([[0, 0], [2, 3], [4, 7], [7, 10], [10, 15]])


# euclidean_distance = np.linalg.norm(positions[-1] - positions[0])
# print("\nEuclidean Distance (first to last):", euclidean_distance)


# step_distances = np.linalg.norm(np.diff(positions, axis=0), axis=1)
# total_distance = np.sum(step_distances)
# print("Total Distance Traveled (step-by-step):", total_distance)











