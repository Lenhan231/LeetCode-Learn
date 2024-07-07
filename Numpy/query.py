import numpy as np
list2 = [[0,1,2], [3,4,5], [6,7,8]]
arr2 = np.array(list2)
print(arr2[:2, :2]) # this is the ',' item so that it query data from 2 first items of the array and searching for the :2 items of each items
arr2 = arr2[::-1, ]
print(arr2) # reserve the item in array not the item in each item
# but we can teserve items in each items like this 
arr2 = arr2[::-1]
arr2 = arr2[::, ::-1]
print(arr2)