# Deleting nodes in a linked list

# initialising node object
class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


# initialising linker object
class Linker:
    def __init__(self):
        self.head = None

    def printnodes(self):
        temp = self.head
        if (temp is None):
            print('List empty')
            return
        else :
            while(temp):
                print(temp.data)
                temp = temp.next
    def DeleteBegining(self):
        temp = self.head
        if(temp is None):
            print('cannot delete elements in empty List')
            return
        else:
            self.head = self.head.next
            temp =None
    def DeleteKey(self, key):
        Nxt = self.head.next
        Prev = self.head
        # check if list is empty
        if (self.head is not None):
            #if previous node is equal to head and previous pointer holds the key
            if (Prev.data == key and Prev == self.head):
                self.head = Nxt
                Prev = None
                return
            else:
                # if NXt node does not hold the key keep traversing
                while (Nxt.data is not key):
                    Nxt = Nxt.next
                    Prev = Prev.next
                # if Nxt holds the key and Nxt is not the last node
                if (Nxt.next is not None):
                        Prev.next = Nxt.next
                        Nxt.next = None

                # if Nxt holds the key and Nxt is the last node
                else:
                    Prev.next = None
                    return
        print('Cannot delete in an empty linked list')
        return


if __name__ == '__main__':

    MyList = Linker()
    MyList.head = Node(10)
    second = Node(20)
    third = Node(30)
    forth = Node(40)

# Linking nodes
    MyList.head.next = second
    second.next = third
    third.next = forth

# call print function
    MyList.printnodes()
    #MyList.DeleteBegining()
    MyList.DeleteKey(40)
    print('after deleting------------------------')
    MyList.printnodes()
