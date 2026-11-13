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
        
#1.4. Добавьте в класс LinkedList метод поиска всех узлов по конкретному значению
    def find_all(self, val):
        res = []
        node = self.head
        while node is not None:
            if node.value == val:
                res.append(node)
            node = node.next
        return res # здесь будет ваш код+++

#1.1. Добавьте в класс LinkedList метод удаления одного узла по его значению
#где флажок all=False по умолчанию -- удаляем только первый нашедшийся элемент.
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
#1.3. Добавьте в класс LinkedList метод очистки всего содержимого
    def clean(self):
        self.head = None
        self.tail = None
        #pass # здесь будет ваш код+++
#1.5. Добавьте в класс LinkedList метод вычисления текущей длины списка
    def len(self):
        res = 0
        node = self.head
        while node is not None:
            res += 1
            node = node.next
        return res # здесь будет ваш код+++
        
#1.6. Добавьте в класс LinkedList метод вставки узла newNode после заданного узла afterNode
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

#1.8. Напишите функцию, которая получает на вход два 
#связанных списка, состоящие из целых значений, и если их длины равны, 
#возвращает список, каждый элемент которого равен сумме 
#соответствующих элементов входных списков. 
def sumItems(linkedList1, linkedList2):
    res = []
    node1 = linkedList1.head
    node2 = linkedList2.head
    if linkedList1.len() != linkedList2.len():
        return res
    while node1 is not None and node2 is not None:
        res.append(node1.value + node2.value)
        node1 = node1.next    
        node2 = node2.next    
    return res    
   
n11 = Node(1)
n12 = Node(2)    
n13 = Node(3)    
n14 = Node(4)    
n15 = Node(5)
ll1 = LinkedList()
ll1.add_in_tail(n11)
ll1.add_in_tail(n12)
ll1.add_in_tail(n13)
ll1.add_in_tail(n14)
ll1.add_in_tail(n15)
ll1.delete(1)
ll1.print_all_nodes()

