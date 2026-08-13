#Importing Numpy Library
import numpy as np

#Creating 0-D Array
arr=np.array(50)
print(arr)

#Creating 1-D Array
arr1 =np.array([1,2,3,4,5,6])
print(arr1)

#checking the type of array
print(type(arr1))

#Creating 2-D Array
arr2 = np.array([[1,2,3],[4,5,6]])
print(arr2)

#Creating 3-D Array
arr3 = np.array([[[1,2,3],[4,5,6]],
                 [[7,8,9],[10,11,12]]])
print(arr3)

#checking the dimension of array
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#Higher Dimensional Arrays
arr4 = np.array([1,2,3,4], ndmin=5)
print(arr4)

#Acessing Array Elements
arr5 = np.array([1,2,3,4,5,6])
print(arr5[0])     

#Acessing elements of 2-D array
arr6 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr6[0,1])#Access the element on the first row, second column    
print('5th element on 2nd row: ', arr6[1, 4])#Access the element on the 2nd row, 5th column:

#Acessing elements of 3-D array
arr7 = np.array([[[1,2,3],[4,5,6]],
                 [[7,8,9],[10,11,12]]])
print(arr7[0,1,2])#Access the element on the first array, second row, third column
print('2nd element on 1st array, 2nd row: ', arr7[1, 0, 1])#Access the element on the second array, first row, second column    

#Negative Indexing
arr8 = np.array([1,2,3,4,5,6])
print(arr8[-1])#Access the last element

arr9= np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr9[1, -1])

#Slicing Arrays
arr10 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr10[1:5])#Elements from index 1 to 4  
print(arr10[4:])#Elements from index 4 to the end
print(arr10[:4])#Elements from the beginning to index 3

#Negative Slicing
arr11 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr11[-3:-1])#Elements from index -3 to -1
print(arr11[-5:])#Elements from index -5 to the end
print(arr11[:-5])#Elements from the beginning to index -5   

#Step in Slicing
arr12 = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr12[1:7:2])#Elements from index 1 to 6, with a step of 2
print(arr12[::3])#Elements from the beginning to the end, with a step of 3  

#Slicing 2-D Arrays
arr13 = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(arr13[1, 1:4])#   Elements from index 1 to 3 from the second row  
#for both elements
print(arr13[0:2, 2]) #o/p [3 8]
#From both elements, slice index 1 to index 4 (not included), this will return a 2-D array:
print(arr13[0:2, 1:4]) #o/p [[2 3 4]
                           #[7 8 9]]

#Datatypes in Numpy
arr14 = np.array([1,2,3,4], dtype='int64')
print(arr14.dtype)

arr15 = np.array(['apple', 'banana', 'cherry'])
print(arr15.dtype) #U6 6-largest string length is 6

#defining data type while creating array
arr16 = np.array([1,2,3,4], dtype='S')#
print(arr16.dtype) #S1 1-largest string length is 1

#defining size of data type while creating array
arr17 = np.array(['apple', 'banana', 'cherry'], dtype='U10')#
print(arr17.dtype) #U10 10-largest string length is 10

#Converting Data Type on Existing Arrays
arr18 = np.array([1.1, 2.1, 3.1])
newarr = arr18.astype('int32')#converting float to int
print(newarr)

#Copying Arrays
#Make a copy, change the original array, and display both arrays
arr19 = np.array([1,2,3,4,5])
x = arr19.copy()#copying arr19 to x
arr19[0] = 42#changing the first element of arr19
print(arr19)#o/p [42  2  3  4  5]
print(x)#o/p [1 2 3 4 5]       

#View
arr20 = np.array([1, 2, 3, 4, 5])
x = arr20.view()
arr20[0] = 42
print(arr20)
print(x)

#View vs Copy
#Make a view, change the original array, and display both arrays
arr21 = np.array([1,2,3,4,5])
y = arr21.view()#viewing arr21 to y     

#Check if y is a copy or a view: The copy owns the data, the view does not.
print(y.base) #o/p [1 2 3 4 5]  
print(arr21.base) #o/p None


#Shape of an Array
arr22 = np.array([[1,2,3,4], [5,6,7,8]])
print(arr22.shape) #o/p (2, 4) 2 rows and 4 columns

arr23 = np.array([1, 2, 3, 4], ndmin=5)
print(arr23) #[[[[[1 2 3 4]]]]]
print('shape of array :', arr23.shape) #(1, 1, 1, 1, 4)

#Reshaping an Array
#1-D to 2-D
arr24 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr24.reshape(4,3)
print(newarr) #o/p [[ 1  2  3]
              #[ 4  5  6]
              #[ 7  8  9]
              #[10 11 12]]  
#1-D to 3-D
newarr = arr24.reshape(2,3,2)
print(newarr) #o/p [[[ 1  2]
              #[ 3  4]
              #[ 5  6]]         

#Unknown Dimension
arr25 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr25.reshape(2,-1,3)
print(newarr) #o/p [[[ 1  2  3]
              #[ 4  5  6]]
             #[[ 7  8  9]
              #[10 11 12]]      

#Flattening the Array
arr26 = np.array([[1,2,3], [4,5,6]])
newarr = arr26.flatten()
print(newarr) #o/p [1 2 3 4 5 6]        

#Iterating Arrays
#1-D Array
arr27 = np.array([1,2,3])
for x in arr27:
  print(x) #o/p 1 2 3  

#Iterating 2-D Arrays
arr28 = np.array([[1,2,3], [4,5,6]])
for x in arr28:
  print(x) #o/p [1 2 3] [4 5 6]
#Iterate on each scalar element of the 2-D array:
for x in arr28:
  for y in x:
    print(y) #o/p 1 2 3 4 5 6

#Iterating 3-D Arrays
arr29 = np.array([[[1,2,3], [4,5,6]], [[7,8,9], [10,11,12]]])
for x in arr29:
  print(x) #o/p [[1 2 3] [4 5 6]] [[ 7  8  9] [10 11 12]]  
#Iterate down to the scalars 3-D array:
for x in arr29:
  for y in x:
    for z in y:
      print(z) #o/p 1 2 3 4 5 6 7 8 9 10 11 12

#Iterating Arrays Using nditer()
arr30 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr30):
  print(x)

#Iterating With Different Step Size
arr31 = np.array([1, 2, 3, 4, 5, 6])
for x in np.nditer(arr31[::2]):
  print(x) #o/p 1 3 5

#Enumerated Iteration Using ndenumerate()
arr32 = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr32):
    print(idx, x)   

#Joining Arrays

#Joining 1-D Arrays
arr33 = np.array([1, 2, 3])
arr34 = np.array([4, 5, 6])
newarr = np.concatenate((arr33, arr34))
print(newarr) #o/p [1 2 3 4 5 6]

#Joining 2-D Arrays
arr35 = np.array([[1, 2], [3, 4]])
arr36 = np.array([[5, 6], [7, 8]])
newarr = np.concatenate((arr35, arr36), axis=0)
print(newarr) #o/p [[1 2] [3 4] [5 6] [7 8]]
#Joining 2-D Arrays Along Rows
newarr = np.concatenate((arr35, arr36), axis=1)
print(newarr) #o/p [[1 2 5 6]
              #[3 4 7 8]]   

#Joining Arrays Using Stack Functions
#Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
#Joining 1-D Arrays
arr37 = np.array([1, 2, 3])
arr38 = np.array([4, 5, 6])
arr = np.stack((arr37, arr38), axis=1)
print(arr)
#Joining 2-D Arrays
arr39 = np.array([[1, 2], [3, 4]])
arr40 = np.array([[5, 6], [7, 8]])
#Stacking along rows (axis=0):
arr = np.stack((arr39, arr40), axis=0)
print(arr) #o/p [[[1 2] [3 4]] [[5 6] [7 8]]]
#Stacking along columns (axis=1):
arr = np.stack((arr39, arr40), axis=1)
print(arr) #o/p [[[1 2] [5 6]] [[3 4] [7 8]]]
#Stacking along the last axis (axis=-1):
arr = np.stack((arr39, arr40), axis=-1)
print(arr) #o/p [[[1 5] [2 6]] [[3 7] [4 8]]]   

#Stacking Along Rows
arr41 = np.array([1, 2, 3])
arr42 = np.array([4, 5, 6])
arr = np.hstack((arr41, arr42)) #[1 2 3 4 5 6]
print(arr)
#Stacking Along Columns
arr43 = np.array([1, 2, 3])
arr44 = np.array([4, 5, 6])
arr = np.vstack((arr43, arr44)) #o/p [[1 2 3] [4 5 6]]
print(arr)

#Stacking Along Height (depth)
arr45 = np.array([[1, 2], [3, 4]])
arr46 = np.array([[5, 6], [7, 8]])
arr = np.dstack((arr45, arr46)) #o/p [[[1 5] [2 6]] [[3 7] [4 8]]]
print(arr)

#Splitting Arrays

#Splitting 1-D Arrays
arr47 = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr47, 3) #o/p [array([1, 2]), array([3, 4]), array([5, 6])]
print(newarr)

#Splitting 2-D Arrays
arr48 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr48, 3) #o/p [array([[1, 2], [3, 4]]), array([[5, 6], [7, 8]]), array([[ 9, 10], [11, 12  ])]  
print(newarr)   

#Splitting 2-D Arrays Into Arrays
arr49 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr49, 3, axis=1) #o/p [array([[ 1], [ 4], [ 7], [10], [13], [16]]), array([[ 2], [ 5], [ 8], [11], [14], [17]]), array([[ 3], [ 6], [ 9], [12], [15], [18]])]
print(newarr)   

#hsplit() will split the array horizontally, vsplit() will split vertically, and dsplit() will split depth wise.    
arr50= np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr50, 3) #o/p [array([[ 1], [ 4], [ 7], [10], [13], [16]]), array([[ 2], [ 5], [ 8], [11], [14], [17]]), array([[ 3], [ 6], [ 9], [12], [15], [18]])]
print(newarr)

# Splitting a 3-D Array
arr51 = np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]],
    [[13, 14], [15, 16]]
])
# Split the 3-D array into 2 arrays along the depth axis
newarr = np.dsplit(arr51, 2)
print(newarr) 


##Searching Arrays
#Finding the Indices of Elements
arr52 = np.array([1, 2, 3, 4, 5, 1, 2, 3])
x = np.where(arr52 == 3)
print(x) #o/p (array([2, 7]),) 3 is present at index 2 and 7    

## Finding the Indices of Elements in a 2-D Array
arr53 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
])
# Find the indices of elements greater than 5
x = np.where(arr53 > 5)
print(x) # Output:
         # (array([1, 1, 1, 2, 2, 2]),
         #  array([1, 2, 3, 0, 1, 2]))

#Find the indexes where the values are odd:
arr54 = np.array([10, 14, 93, 41, 8, 7])
x = np.where(arr54%2 == 1)
print(x)

#SearchSorted
arr55 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr55, 7)
print(x)

#Search From the Right Side
arr56 = np.array([6, 7, 8, 9])
x = np.searchsorted(arr56, 7, side='right')
print(x)

#Multiple Values
arr57 = np.array([1, 3, 5, 7])
x = np.searchsorted(arr57, [2, 4, 6])
print(x) 

#Sorting Array
arr58= np.array([3, 2, 0, 1])
print(np.sort(arr58))

#Sort the array alphabetically:
arr59 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr59))

#Sort a boolean array:
arr60 = np.array([True, False, True])
print(np.sort(arr60))

#Sorting a 2-D Array
arr61 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr61)) #o/p [[2 3 4]
                          #[0 1 5]]

#Filtering Array
arr62 = np.array([41, 42, 43, 44])
x = [True, False, True, False] #Create an array from the elements on index 0 and 2:
newarr = arr62[x]
print(newarr) #o/p [41 43]

#Creating Filtering Array
arr63 = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = [] # Create an empty list
# go through each element in arr
for element in arr63: # go through each element in arr
  if element % 2 == 0: # if the element is completely divisble by 2, set the value to True, otherwise False
    filter_arr.append(True)
  else:
    filter_arr.append(False)
newarr = arr63[filter_arr]
print(filter_arr)
print(newarr)