class Node:

    def __init__(self, v):
        self.value = v
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

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
        return res # здесь будет ваш код+++

    def delete(self, val, all=False):
        node = self.head
        prev_node = None
        while node is not None:
            if node.value == val:
                prev_node.next = node.next
                node = prev_node.next
                if all != True:
                   return None
            else:       
                prev_node = node       
                node = node.next            
        return None # здесь будет ваш код+++

    def clean(self):
        self.head = None
        self.tail = None
        #pass # здесь будет ваш код+++

    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res # здесь будет ваш код+++

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode == None:
            newNode.next = self.head
            self.head = newNode
        while node is not None:
            if node == afterNode:
                tmp = node.next 
                node.next = newNode
                newNode.next = tmp
            node = node.next    
        return None # здесь будет ваш код
    
n1 = Node(1)
n2 = Node(2)    
n3 = Node(3)    
n4 = Node(4)    
n5 = Node(5)
n55 = Node(5)
ll = LinkedList()
#ll.print_all_nodes()
ll.add_in_tail(n1)
ll.add_in_tail(n2)
ll.add_in_tail(n3)
ll.add_in_tail(n4)
ll.add_in_tail(n5)
ll.insert(None, n55)
# ll.delete(3)
# ll.delete(5,all=True)
# #ll.clean()
# print(ll.len())
ll.print_all_nodes()
#print(ll.find_all(5))
