class Node:
    def __init__(self,value):
        self.value = value 
        self.next = None 
        

class LinkedsList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
    
    def insert(self, value):
        temp  = self.head 
        while temp.next:
            temp = temp.next 
        temp.next = Node(value)
