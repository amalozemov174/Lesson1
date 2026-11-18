class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

class LinkedList2:  
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res

    def delete(self, val, all=False):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                if node.prev == None:
                    if node.next == None:
                        self.tail = None
                    self.head = node.next                    
                    node = node.next
                    node.prev.next = None
                    node.prev = None
                elif node.next == None:    
                    node.prev.next = None
                    self.tail = node.prev
                    tmp = node
                    node = node.next
                    tmp.prev = None
                    tmp.next = None
                else:
                    tmp = node
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    node = node.next
                    tmp.prev = None
                    tmp.next = None
                if all != True:
                   return None
            else:       
                prev_node = node       
                node = node.next            
        return None

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res

    def insert(self, afterNode, newNode):
        pass # здесь будет ваш код

    def add_in_head(self, newNode):
        if newNode != None:
            if self.head != None:
                tmp = self.head
                self.head = newNode
                newNode.prev = None
                newNode.next = tmp
                tmp.prev = newNode
            else:
                self.head = newNode
                self.tail = newNode            
