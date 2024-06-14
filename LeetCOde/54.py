a = [1,0,-1,0,-2,2]
b = []
target = 0
for i in range(len(a)):
    j = i + 1
    while j + 2 < len(a):
        if target == a[i] + a[j] + a[j+1] + a[j+2]:
            c = [a[i], a[j], a[j+1], a[j+2]]
            b.append(c)
        j += 1
print(b)


        