def delete(head, point):
    count = 0 
    current = head
    while current:
        if count != point - 1:
            current = current.next
            count += 1
        else:
            k = current.next
            current = k.next
            break
    return head