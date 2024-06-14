current = head
    while current.next != head:
        print(current.next)
        print(current)
        print("---")
        current = current.next
        count += 1