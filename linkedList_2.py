def reverse_linked_list(linkedList):
    if linkedList.len() <= 1:
        return linkedList
    node = linkedList.head
    while node is not None:
        if node is not None:
            tmp = node
            node_next = tmp.next
            node_prev = tmp.prev
            if node.next is not None and node.prev is not None:
                node.next = node_prev
                node.prev = node_next
                node = node_next
            else:
                if node_next is None:
                    node.next = tmp.prev
                    node.prev = None
                    node = node_next
                    linkedList.head = tmp
                if node_prev is None:
                    node.prev = tmp.next
                    node.next = None
                    node = node_next
                    linkedList.tail = tmp
