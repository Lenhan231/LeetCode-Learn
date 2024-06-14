seats = [1,2,6,6]
students = [2,3,2,6]
nodes = []
class Attr:
    def __init__(self, val, label):
        self.val = val
        self.label = label

seats = sorted(seats)
students = sorted(students)
while seats and students:
    if seats[0] < students[0]:
        nodes.append(Attr(seats.pop(0), "seat"))
    else:
        nodes.append(Attr(students.pop(0), "student"))

while seats:
    nodes.append(Attr(seats.pop(0), "seat"))
while students:
    nodes.append(Attr(students.pop(0), "student"))

sum = 0
while nodes:
    if nodes[0].label == "student":
        for i in range(len(nodes)):
            if nodes[i].label == "seat":
                sum = sum + (nodes.pop(i).val - nodes.pop(0).val)
                break
    else:
        for i in range(len(nodes)):
            if nodes[i].label == "student":
                sum = sum + (nodes.pop(i).val - nodes.pop(0).val)
                break
print(sum)