lst = []
for i in range(int(input())):
    lst.append(input())
class dbl:
    def __init__(self, val = 0 , next = None, prev = None):
        self.next = next 
        self.prev = prev
        self.val = val

def create(lst):
    head = dbl()
    current = head
    for i in lst:
        current.next = dbl(i)
        temp = current
        current = current.next
        current.prev = temp
    return head.next

def append(lst, id, val):
    index = -1
    current = lst
    check = 0
    while (index != id or current) and current is not None:
        if index + 1 == id:
            node = dbl(val)
            temp = current.prev
            current.prev = node
            temp.next = node
            node.next = current
            check = 1
        temp = current
        current = current.next
        index += 1

    if current is None and check == 0:
        current = temp
        current.next = dbl(val)
        current = current.next
        current.prev = temp

    if id == 0:
        return lst.prev
    return lst
    

a = append(create(lst), int(input()), input())

while a:
    print(a.val, end = " ")
    a = a.next