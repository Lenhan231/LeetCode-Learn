s = ['a','b','c','d']
numRows = 3
j = 0
a = [[" " for j in range(numRows)] for i in range(numRows)]
id = 0
j = 0
for i in range(numRows):
    if id < len(s):
        if i + 1 % numRows == 0 or i == 0:
            while j != numRows - 1 and id < len(s):
                a[i][j] = s[id]
                id += 1
        else:
            while j != 0 and id < len(s):
                a[i][j] = s[id]
                id += 1
    
print(a)

    