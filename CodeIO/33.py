a = [1, 1, 2, 3, 4, 5, 5]
def min(a):
    min = a[0]
    current = 0
    for i in range(len(a)):
        if min > a[i]:
            min = a[i]
            current = i
    return current

def max(a):
    max = a[0]
    for i in range(len(a)):
        if max < a[i]:
            max = a[i]
            current = i 
    return current

b = max(a)
c = min(a)

a[b], a[c] = a[c], a[b] 
print(a)

