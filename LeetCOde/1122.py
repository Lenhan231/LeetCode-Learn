arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
arr3 = []
for i in arr2:
    j = 0
    while i in arr1:
        if arr1[j] == i:
            arr3.append(arr1.pop(j))
        j += 1
arr1 = sorted(arr1)
for j in arr1:
    arr3.append(j)
print(arr3)
