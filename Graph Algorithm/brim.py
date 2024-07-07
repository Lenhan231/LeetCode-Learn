'''arr = [23, 1, 10, 5, 2]
for i in range(1, len(arr)):
    key = arr[i]
    j = i-1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j] = key

print(arr)
'''
 