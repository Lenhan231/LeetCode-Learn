class ha:
    def __init__(self, value, dig):
        self.dig = dig
        self.value = value 

count = 0 
list = []
listcheck = []
for i in "whatthefack":
    if i not in listcheck:
        listcheck.append(i)
        list.append(ha(i,count))
        count += 1 

for i in list:
    print(f"{i.value} {i.dig}")