class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        l3 = ListNode()
        cur = l3
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            carry = v1 + v2 + carry
            l1 = l1.next if l1 else 0
            l2 = l2.next if l2 else 0
            if carry >= 10:
                cur.next = ListNode(carry%10)
                cur = cur.next
            else:
                cur.next = ListNode(carry)
                cur = cur.next
            carry = carry//10
        return l3