# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Singly Linked List

class LinkedList:

    class Node:
        
        def __init__(self, value, next_pointer = None): 
            self.value = value
            self.next_pointer = next_pointer

    
    def __init__(self):
        self.head = None 

    
    def insert(self, item):
        self.head = LinkedList.Node(item, self.head)

    def print_item(self):
        if self.head == None:
            return ""
        else:
            current = str(self.head.value)
            next_pointer = self.head.next_pointer
            while next_pointer != None:
                current += " " + str(next_pointer.value)
                next_pointer = next_pointer.next_pointer 
            return current
        
    
    def append(self, item):
        new_node = LinkedList.Node(item)
        if self.head == None:
            self.head = new_node
        else:
            current = self.head
            while current.next_pointer != None:
                current = current.next_pointer
            current.next_pointer = new_node