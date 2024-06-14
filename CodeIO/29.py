lst = [1,2,3,4]
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
    return head.next

def delete(head, id):
    current = head
    count = 0
    if id == 0:
        return head.next
    while count != id and current.next is not None:
        if count + 1 == id:
            current.next = current.next.next
        current = current.next 
        count += 1 
    return head
    
a = delete(create(lst),)
while a:
    print(a.val, end = " ")
    a = a.next

