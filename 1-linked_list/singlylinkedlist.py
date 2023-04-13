# Author PAUL OFFEI
# Date 4/11/2023
# Program Description: Singly Linked List (Another Implementation style)

class Node:
    """
    A Node object for holding data and reference in a link representation

    Constructor Parameter
    --------------------------
        Data: any (private)  hold any value of any data type
        Next: None (private) hold reference or pointer or address to the previous node object
    """

    def __init__(self, data):
        self.data = data
        self.next = None
    



class LinkedList:
    """
    A Link object for connecting the Node object into a single link list

    Constructor Parameter
    -------------------------
        Head: None (private) hold the reference or address or pointer to all Node object created
        Size: int (private) hold or count the number of Node object in alive 
    """

    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size 
    

    def add(self, item):
        """
        Parameter
        --------------
            Item: any
                Add new node object containing a value of this item to the beginning of the linked list
        """
        new_node = Node(item)
        previous_head = self.head
        self.head = new_node
        new_node.next = previous_head
        self.size += 1 

    
    def remove_first(self):
        """
        Remove the first node object and return the item in it and also return None if the node object is empty 
        """
        result = None
        if self.head:
            result = self.head.data
            self.head = self.head.next
            self.size -= 1
        return result
    

    def add_last(self, item):
        """
        Parameter
        --------------
            Item: any
                Add new node object containing a value of this item to the ending of the linked list
        """
        new_node = Node(item)
        node = self.head
        while node.next:
            node = node.next
        node.next = new_node
        self.size += 1


    def __str__(self):
        result = ""
        node = self.head
        if node == None:
            result += str(node)
            return result
        else:
            while node:
                result += f"{node.data} ===> "
                node = node.next    
            return result 

