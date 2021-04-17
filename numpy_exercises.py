import numpy as np
import math
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])

# How many negative numbers are there?
print(f"There are {np.count_nonzero(a < 0)} negative numbers.")
# There are 4 negative numbers.

# How many positive numbers are there?
print(f"There are {np.count_nonzero(a > 0)} positive numbers.")
# There are 5 positive numbers.

# How many even positive numbers are there?
print(f"There are {np.count_nonzero((a > 0) & (a % 2 == 0))} positive even numbers.")
# There are 3 positive even numbers.

# If you were to add 3 to each data point, how many positive numbers would there be?
b = a + 3
print(f"There are {np.count_nonzero(b > 0)} positive numbers.")
# There are 10 positive numbers.

# If you squared each number, what would the new mean and standard deviation be?
c = b ** 2
print(f"The mean is: {np.mean(c)}")
print(f"The standard deviation is: {np.std(a)}")
# The mean is: 101.0
# The standard deviation is: 8.06225774829855

# A common statistical operation on a dataset is centering. This means to adjust the data such that the 
# mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. 
d = a - np.mean(a)
# array([  1.,   7.,   9.,  20.,  -5.,  -4.,  -3.,  -3.,  -3.,  -9.,   0., -10.])
np.mean(d)
# 0.0

# Calculate the z-score for each data point.
e = (a - np.mean(a)) / np.std(a)
# array([ 0.12403473,  0.86824314,  1.11631261,  2.48069469, -0.62017367,
#        -0.49613894, -0.3721042 , -0.3721042 , -0.3721042 , -1.11631261,
#         0.        , -1.24034735])

## Setup 1
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use python's built in functionality/operators to determine the following:
# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a = np.sum(a)
print(f"The sum is: {sum_of_a} ")

# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a = np.min(a)
print(f"The min is: {min_of_a}")

# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a = np.max(a)
print(f"The max is: {max_of_a}")

# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a = np.mean(a)
print(f"The mean is: {mean_of_a}")

# Exercise 5 - Make a variable named product_of_a to hold the product of multiplying all the numbers in the 
# above list together
product_of_a = np.prod(a)
print(f"The product is: {product_of_a}")

# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like 
# [1, 4, 9, 16, 25...]
squares_of_a = np.square(a)
print(f"The squares of a are: {squares_of_a}")

# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a = np.array(a[(a % 2) == 1])
print(f"The odds of a are: {odds_in_a}")

# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.
evens_in_a = np.array(a[(a % 2) == 0])
print(f"The evens in a are: {evens_in_a}")

## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares 
# for this list of two lists.
b = np.array([
    [3, 4, 5],
    [6, 7, 8]
])

# Exercise 1 - refactor the following to use numpy. Use sum_of_b as the variable. 
# **Hint, you'll first need to make sure that the "b" variable is a numpy array**
# sum_of_b = 0
# for row in b:
#     sum_of_b += sum(row)
sum_of_b = np.sum(b)
print(f"The sum of b is: {sum_of_b}")

# Exercise 2 - refactor the following to use numpy. 
# min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  
min_of_b = np.min(b)
print(f"The min of b is: {min_of_b}")

# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
# max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])
max_of_b = np.max(b)
print(f"The max of b is: {max_of_b}")

# Exercise 4 - refactor the following using numpy to find the mean of b
# mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))
mean_of_b = np.mean(b)
print(f"The mean of b is: {mean_of_b}")

# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied 
# together.
# product_of_b = 1
# for row in b:
#     for number in row:
#         product_of_b *= number
product_of_b = np.prod(b)
print(f"The product of b is: {product_of_b}")

# Exercise 6 - refactor the following to use numpy to find the list of squares 
# squares_of_b = []
# for row in b:
#     for number in row:
#         squares_of_b.append(number**2)
squares_of_b = np.square(b)
print(f"The squares of b are: {squares_of_b}")

# Exercise 7 - refactor using numpy to determine the odds_in_b
# odds_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 != 0):
#             odds_in_b.append(number)
odds_in_b = np.array(b[(b % 2) == 1])
print(f"The odds in array b are: {odds_in_b}")


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
# evens_in_b = []
# for row in b:
#     for number in row:
#         if(number % 2 == 0):
#             evens_in_b.append(number)
evens_in_b = np.array(b[b % 2 == 0])
print(f"The evens in the array are: {evens_in_b}")

# Exercise 9 - print out the shape of the array b.
print (f"The shape of b is: {np.shape(b)}")

# Exercise 10 - transpose the array b.
print(f"Transpose the array: {np.transpose(b)}")

# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)
np.reshape(b, (1, 6))

# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)
np.reshape(b, (6, 1))

## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array 
# methods.
# Exercise 1 - Find the min, max, sum, and product of c.
min_of_c = np.min(c)
max_of_c = np.max(c)
sum_of_c = np.sum(c)
prod_of_c = np.prod(c)
print(f"The min of c is: {min_of_c}")
print(f"The max of c is: {max_of_c}")
print(f"The sum of c is: {sum_of_c}")
print(f"The product of c is: {prod_of_c}")

# Exercise 2 - Determine the standard deviation of c.
std_of_c = np.std(c)
print(f"The standard deviation of c is: {std_of_c}")

# Exercise 3 - Determine the variance of c.
var_of_c = np.var(c)
print(f"The variance of c is: {var_of_c}")

# Exercise 4 - Print out the shape of the array c
print (f"The shape of c is: {np.shape(c)}")

# Exercise 5 - Transpose c and print out transposed result.
print(f"Transpose the array: {np.transpose(c)}")

# Exercise 6 - Get the dot product of the array c with c.
print(f"The dot product of c and c is: {np.dot(c, c)}") 

# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261
print(f"The result of c times c transposed is: {(c * np.transpose(c)).sum()}")

# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 
# 131681894400.
print(f"The result of c times c transposed is: {(c * np.transpose(c)).prod()}")

## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]

# Exercise 1 - Find the sine of all the numbers in d
print(f"The sine of the numbers is: {np.sin(d)}")

# Exercise 2 - Find the cosine of all the numbers in d
print(f"The cosine of the numbers is: {np.cos(d)}")

# Exercise 3 - Find the tangent of all the numbers in d
print(f"The tangent of the numbers is: {np.tan(d)}")

# Exercise 4 - Find all the negative numbers in d
d = np.array([[90, 30, 45, 0, 120, 180],
[45, -90, -30, 270, 90, 0],
[60, 45, -45, 90, -45, 180]])
neg_in_d = d[d < 0]

# Exercise 5 - Find all the positive numbers in d
pos_in_d = d[d > 0]
print(f"The positive numbers in d are: {pos_in_d}")

# Exercise 6 - Return an array of only the unique numbers in d.
print(f"The unique numbers of array d are: {np.unique(d)}")

# Exercise 7 - Determine how many unique numbers there are in d.
e = np.unique(d)
print(f"The number of unique numbers are: {len(e)}")

# Exercise 8 - Print out the shape of d.
print (f"The shape of d is: {np.shape(d)}")

# Exercise 9 - Transpose and then print out the shape of d.
e = np.transpose(d)
print (f"The shape of e is: {np.shape(e)}")

# Exercise 10 - Reshape d into an array of 9 x 2
np.reshape(d, (9, 2))