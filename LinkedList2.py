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
                    else:
                        node.next.prev = None    
                    self.head = node.next                    
                    node = node.next
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
        node = self.head
        if newNode == None:
            return None
        if afterNode == None:
            if self.tail is None and self.head is None:
                self.head = newNode
                self.tail = newNode
                newNode.prev = None
                newNode.next = None
            else:    
                self.tail.next = newNode
                newNode.prev = self.tail
                newNode.next = None
                self.tail = newNode
            return None        
        while node is not None:
            if node == afterNode:
                if node.next == None:
                    self.tail = newNode
                    newNode.next = None
                    newNode.prev = node
                    node.next = newNode
                else:                    
                    tmp = node.next 
                    node.next = newNode
                    newNode.next = tmp
                    newNode.prev = node
                    tmp.prev = newNode
                if node == self.tail:
                    self.tail = newNode
                return None    
            node = node.next    
        return None

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
