class dbl:
    def __init__(self, val = 0 , next = None, prev = None):
        self.next = next 
        self.prev = prev
        self.val = val

def append():
    head = dbl(1)
    current = head
    for i in range(2, 3 + 1):
        current.next = dbl(i)
        temp = current
        current = current.next
        current.prev = temp
    return current

a = append()
while a.prev:
    print(a.val, end = " ")
    a = a.prev
while a:
    print(a.val, end = " ")
    a = a.next
   


    