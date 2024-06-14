class LN:
    def __init__(self, val = 0 , next = None):
        self.val = val
        self.next = next

def node():
    head = LN()
    current = head
    for i in [1,1,2,2,3,3]:
        current.next = LN(i)
        current = current.next
    return head.next

a = node()
while a is not None:
    print(a.val)
    a = a.next