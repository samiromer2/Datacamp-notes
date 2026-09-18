#list.index
#list.count
#str.capitaliza()
#str.replace("z","as")
#list.append("me")
#type(object)
#packages -> numpy, pandas, matplotlib , scikit-learn, seaborn, tensorflow, keras, pytorch
#get pip
#get-pip
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full)

# Print out full_sorted
print(full_sorted)

#-------------------------
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full,reverse=True)

# Print out full_sorted
print(full_sorted)

#-------
# string to experiment with: place
place = "poolhouse"

# Use upper() on place
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)


# Print out the number of o's in place
print(place.count('o'))

# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas.index(20.0))

# Print out how often 9.50 appears in areas
print(areas.count(9.50))


# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)


# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)


#----
# Import the math package
import math

# Calculate C
C = 2 * 0.43 * math.pi

# Calculate A
A = math.pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))



#---------
# Import pi function of math package
from math import pi

# Calculate C
C = 2 * 0.43 * pi

# Calculate A
A = pi * 0.43 ** 2

print("Circumference: " + str(C))
print("Area: " + str(A))

#----------

#Numpy

# Import the numpy package as np
import numpy as np

baseball = [180, 215, 210, 210, 188, 176, 209, 200]

# Create a numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out type of np_baseball
print(type(np_baseball))


# Import numpy
#import numpy as np
height_in = [180, 215, 210, 210, 188, 176, 209, 200]
# Create a numpy array from height_in: np_height_in
np_height_in = np.array(height_in)

# Print out np_height_in
print(np_height_in)

# Convert np_height_in to m: np_height_m
np_height_m = np_height_in * 0.0254

# Print np_height_m
print(np_height_m)


##import numpy as np

np_weight_lb = np.array(weight_lb)
np_height_in = np.array(height_in)

# Print out the weight at index 50
print(np_weight_lb[50])

# Print out sub-array of np_height_in: index 100 up to and including index 110
print(np_height_in[100:111])


##------------------
##import numpy as np

baseball = [[180, 78.4],
            [215, 102.7],
            [210, 98.5],
            [188, 75.2]]

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the type of np_baseball
print(type(np_baseball))

# Print out the shape of np_baseball
print(np_baseball.shape)

##############
#import numpy as np

# Create a 2D numpy array from baseball: np_baseball
np_baseball = np.array(baseball)

# Print out the shape of np_baseball
print(np_baseball.shape)

##############

import numpy as np

np_baseball = np.array(baseball)

# Print out the 50th row of np_baseball
print(np_baseball[49,:])

# Select the entire second column of np_baseball: np_weight_lb
np_weight_lb = np_baseball[:,1]

# Print out height of 124th player
print(np_baseball[123,0])

import numpy as np

np_baseball = np.array(baseball)

# Print out addition of np_baseball and updated
print(np_baseball + updated )

# Create numpy array: conversion
conversion = np.array([0.0254,0.453592,1])

# Print out product of np_baseball and conversion
print(np_baseball*conversion)
#------------
import numpy as np

# Create np_height_in from np_baseball 
np_height_in = np_baseball[:,0]

# Print out the mean of np_height_in
print(np_height_in.mean())

# Print out the median of np_height_in
print(np.median(np_height_in))

##-----------------

avg = np.mean(np_baseball[:,0])
print("Average: " + str(avg))

# Print median height
med = np.median(np_baseball)
print("Median: " + str(med))

# Print out the standard deviation on height
stddev = np.std(np_baseball[:,0])
print("Standard Deviation: " + str(stddev))

# Print out correlation between first and second column
corr = np.corrcoef(np_baseball[:,0],np_baseball[:,1])
print("Correlation: " + str(corr))


# NumPy subsetting 

# bmi 
# bmi[1]
# bmi > 23 true and false values
# bmi[bmi > 23] the data
#np_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
#np_2d.shape

# Your recent learnings

# When you left 16 hours ago, you worked on NumPy, chapter 4 of the course Introduction to Python. Here is what you covered in your last lesson:

# You learned about the fundamentals of NumPy, a powerful Python package for data science, and how it can efficiently handle array operations. Here are the key points you covered:

#     Introduction to NumPy: You discovered that NumPy arrays are an alternative to Python lists, allowing for fast, element-wise calculations.
#     Creating NumPy Arrays: You used np.array() to convert Python lists into NumPy arrays.

#     import numpy as np
#     np_baseball = np.array(baseball)

#     Element-wise Operations: You learned that operations on NumPy arrays are performed element-wise, unlike Python lists.

#     np_height_m = np_height_in * 0.0254

#     Type Consistency: NumPy arrays require all elements to be of the same type, converting different types to a common one if necessary.
#     Array Arithmetic: Arithmetic operations like +, -, *, and / behave differently with NumPy arrays compared to Python lists.

#     result = np.array([True, 1, 2]) + np.array([3, 4, False])

#     Subsetting: You practiced subsetting NumPy arrays using square brackets and boolean arrays.

#     print(np_height_in[100:111])

# These concepts form the foundation for efficient data manipulation and analysis using NumPy.

# The goal of the next lesson is to advance your skills in analyzing and manipulating data using NumPy's 2D arrays for more complex data analysis tasks.

#numpy.ndarry

# np_2d[0][2]
# np_2d[0,2]

#Generate data 

height = np.round(np.random.normal(1.75, 0.20, 5000),2)

weight = np.round(np.random.normal(70, 10, 5000),2)

npclass = np.column_stack((height,weight))

print(npclass)