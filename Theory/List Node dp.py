class ListNode():
    def __init__(self, val = 0 ,next = None):
        self.val = val
        self.next = next

l = ListNode(1)
current = l
current.next = ListNode(1)
current = current.next
n = int(input()) - 2
while n:
    current.next = ListNode(l.val + current.val)
    l = l.next
    current = current.next
    n -= 1
print(current.val)