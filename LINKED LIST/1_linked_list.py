# Create a linked list from a given list .




# creating a node class
class node:
    def __init__(self, data=None, next=None):
        self.data = data    # value stored in the node
        self.next = next    # reference for next node

# creating a linked list class
class LinkedList:
    def __init__(self):
        self.head = None  # defining head as None initially

    def create_from_list(self, list_data):
        for data in list_data:
            self.append(data)

    def append(self, data):
        new_node = node(data)   # next = None by default

        if self.head is None:
            self.head = new_node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = new_node

    def display(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        while itr:
            print(itr.data, end="-->")
            itr = itr.next
        print("None")   # to mark end of the linked list


# Example usage
num = [10, 89, 9, 56, 56]
ll = LinkedList()
ll.create_from_list(num)
ll.display()
