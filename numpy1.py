import numpy as np

# NUMPY(numericalp)

# . numerical python is an essential python library for numerical computing.
# . it is widely used in data analytics,data science,machine 
# learning,artificial intelligence


# print(np.__version__)

# * np.array() converts a python list into a numpy array.the array type is ndarray

# numbers = np.array([10,20,30,40,50])

# print(numbers)
# print(type(numbers))

# * zeros() creates an array of zeros

# a=np.zeros(5)
# print("zeros:",a)

# * ones()creates an array of ones.

# b=np.ones(5)
# print("ones:",b)

# arrange()generates values using a start,stop,and optional step

# c=np.arange(1,11)
# print("range:",c)

# d=np.arange(2,21,2)
# print("range with step:",d)

# e=np.arange(1,21,2)
# print("range with step:",e)


# * linspace()generate a specified number of evenly spaced values
 
# e=np.linspace(1,10,5)
# print("linspace:",e)

# * one dimensional and two-dimensional array

# a=np.array([10,20,30,40])
# b=np.array([[10,20,30],[40,50,60]])

# print("1d array:")
# print(a)

# print("2d array:")
# print(b)

# print("dimensions:",a.ndim)
# print("shape:",a.shape)
# print("total elements:",a.size)

# print("dimensions:",b.ndim)
# print("shape:",b.shape)
# print("total elements:",b.size)
 
# shape return the number of rows and columns ,while size returns the 
# total number of elements

# a=np.array([10,2,30])
# b=np.array([1.5,2.5,3.5])
# c=np.array([True,False,True])
# z=np.array(5)


# print(a.dtype)
# print(b.dtype)
# print(c.dtype)
# print(z.dtype)


# * access array elements using indexing

# marks=np.array([75,82,68,91,88])
# print("first marks:",marks[0])
# print("third marks:",marks[2])
# print("last marks:",marks[-1])

# marks[1]=95
# print("updated marks:",marks)



#  work


# 1. marks = np.array([75, 82, 68, 91, 88])
# print("Marks:", marks)

# zeros = np.zeros(5)
# print("Five zeros:", zeros)

# ones = np.ones(5)
# print("Five ones:", ones)

# numbers = np.arange(10, 21)
# print("Numbers from 10 to 20:", numbers)

# even_numbers = np.arange(2, 21, 2)
# print("Even numbers from 2 to 20:", even_numbers)

# values = np.linspace(0, 100, 5)
# print("Five equally spaced values:", values)


# 2. student_marks = np.array([[75, 82, 68],[91, 88, 95],[65, 72, 80]])
# print("Student Marks:")
# print(student_marks)


# 3 .import numpy as np

# student_marks = np.array([80, 85, 90, 75, 95])

# print("Number of dimensions:", student_marks.ndim)
# print("Shape of the array:", student_marks.shape)
# print("Total number of elements:", student_marks.size)
# print("Data type of the array:", student_marks.dtype)


# 4. import numpy as np

# marks = np.array([80, 85, 90, 75, 95])

# print("First mark:", marks[0])
# print("Third mark:", marks[2])
# print("Last mark:", marks[-1])
# print("Second-last mark:", marks[-2])

# marks[1] = 90
# marks[-1] = 95

# print("Updated array:", marks)


# 5. import numpy as np

# ages = np.array([18, 20, 19, 21, 18])

# print("First age:", ages[0])
# print("Last age:", ages[-1])

# ages[2] = 22

# print("Updated array:", ages)
# print("Shape:", ages.shape)
# print("Size:", ages.size)
# print("Dimensions:", ages.ndim)
# print("Data type:", ages.dtype)


# * array slicing
# syntax array[start:stop:step].the stop index is excluded.

# numbers = np.array([10,20,30,40,50,60])
# print(numbers[1:4])
# print(numbers[3:])
# print(numbers[::2])
# print(numbers[::-1])


# * access elements in two-dimensional array

# marks =np.array([[80,85,90],[70,75,80],[90,95,85]])

# print("first row:",marks[0])
# print("second row,third subject:",marks[1,2])
# print("first column:",marks[:,0])                      * all rows,first column
# print(marks[:2,:])                        *first two rows,all columns



# * perform arithmetic operations

# a=np.array([10,20,30])
# b=np.array([1,2,3])

# print("addition:",a+b)
# print("Subtraction:", a - b)
# print("Multiplication:", a * b)
# print("Division:", a / b)
# print("power:",a**2)


# * reshape an array

# numbers=np.array(1, 13)
# matrix=numbers.reshape(3,4)

# print(numbers)
# print(matrix)
# print("shape:",matrix.shape)


# * join two arrays

# a=np.array([10,20,30])
# b=np.array([40,50,60])

# print("concatenate:",np.concatenate((a,b)))
# print("vertical stack:",np.vstack((a,b)))
# print("horizontal stack:",np.hstack((a,b)))


# * filter values using conditions

# marks=np.array([45,78,32,90,65,28,85])

# passed=marks[marks>=40]
# failed=marks[marks<40]
# high_scores=marks[marks>=80]
# print("passed:",passed)
# print("failed:",failed)
# print("high_scores:",high_scores)