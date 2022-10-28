# Creating a singly linked list
# class Node initialises the Node objct
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# class to initialize the Link Object
class LinkedList:
    def __init__(self):
        LinkedList.head = None
    def PrintList(self):
        Temp = self.head
        while(Temp):
            print(Temp.data)
            Temp = Temp.next  # traversing
#inserting a node at the beginning of a list
    def Push(self, new_data):
        Temp = Node(new_data)
        Temp.next = self.head
        self.head = Temp

# inserting a node after a specified node
    def InsertAfter(self, prev_node, new_data):
        if prev_node is None :
            print('The list is empty')
            return
        Temp = Node(new_data)
        Temp.next = prev_node.next
        prev_node.next = Temp
# inserting
    def InsertingEnd(self, new_data):
        Temp = Node(new_data)
        if self.head is None:
            self.head = Temp
            return

        last = self.head
        while(last.next):
            last = last.next
        last.next = Temp

# This is where the program will start execution
if __name__ == '__main__':
    Mylist = LinkedList()
    Mylist.head = Node(1)  # creates head pointer pointing to node 1
    second = Node(2)
    third = Node(3)
    # Linking the nodes
    Mylist.head.next = second
    second.next = third
    # calling the prind function
    Mylist.Push(100)
    Mylist.InsertAfter(Mylist.head.next, 300)
    Mylist.InsertingEnd(20)
    Mylist.PrintList()
