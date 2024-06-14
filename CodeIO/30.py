lst = [1]
'''for i in range(int(input())):
    lst.append(input())'''
class node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

def create(lst):
    head = node()
    current = head
    for i in lst:
        current.next = node(i)
        current = current.next
    current.next = head.next
    return head

def nodeID(head, id):
    count = 0
    current = head
    if count == id:
        temp = current
    while current.next != head:
        count += 1
        current = current.next
        if count == id:
            temp = current
    return temp, count


current, count = nodeID(create(lst).next, 0) 
for i in range(count + 1):
    print(current.val, end = " ")
    current = current.next