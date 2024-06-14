a = []
for i in range(int(input())):
    a.append(int(input()))

class node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def LinkedList(a):
    head = node()
    current = head
    for i in a:
        current.next = node(i)
        current = current.next
    head = head.next
    return head

def xoa(head, a):
    # Handle the case where thelast node is the one that needs to be removed
    while head and head.val > a:
        head = head.next
    current = head
    while current and current.next:
        if current.next.val > a:
            current.next = current.next.next
        else:
            current = current.next

    return head

def get(id, current):
    count = 0
    value = current.val
    while count != id:
        current = current.next
        value = current.val
        count += 1
    return value

head = xoa(LinkedList(a), get(int(input()),LinkedList(a)))
while head:
    print(head.val, end = " ")
    head = head.next