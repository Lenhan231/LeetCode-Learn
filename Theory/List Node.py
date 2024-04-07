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

