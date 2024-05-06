class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val # link the memory address not the value
        self.next = next

def create_linked_list(lst):
    head = ListNode(lst[0])
    current = head # Give the head data from current but not travel through the data
    for val in lst[1:]: # Give the current the data flow 
        current.next = ListNode(val)
        current = current.next
    return head # Head start at the begining with full data from the current

def delete(head, o):
    current = head
    while current:
        if current.val > o:
            current.val = current.next.val                                      
            current.next
        else:
            current = current.next
        
    return head

arr = [1, 1, 2, 2, 3, 3]
head = create_linked_list(arr) # node 2 if only if 4 out
head = delete(head, 2)
while head:
    print(head.val, end = " ")
    head = head.next