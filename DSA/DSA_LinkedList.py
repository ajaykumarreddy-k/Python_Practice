#SINGLE LINKED LIST IMPLEMENTATION IN PYTHON
# Node class represents a single node in the linked list.

class Node:
    def __init__(self, data):
        """
        Initializes a new Node with the given data.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data  # Stores the data of the node
        self.next = None  # Pointer to the next node, initialized to None

# SinglyLinkedList class represents the linked list itself.
class SinglyLinkedList:
    def __init__(self):
        """
        Initializes an empty SinglyLinkedList.
        """
        self.head = None  # The head of the list, initially None for an empty list

    def insert(self, data):
        """
        Inserts a new node with the given data at the end of the linked list.

        Args:
            data: The data to be inserted into a new node.
        """
        new_node = Node(data)  # Create a new Node object

        # If the list is empty, make the new node the head
        if not self.head:
            self.head = new_node
            return

        # Traverse to the end of the list
        temp = self.head
        while temp.next:
            temp = temp.next
        
        # Link the new node to the last node
        temp.next = new_node
    def display(self):
        """
        Displays the data in the linked list.
        """
        temp = self.head  # Start from the head
        while temp:  # Traverse until the end of the list
            print(temp.data, end=" -> ")  # Print the data of each node
            temp = temp.next  # Move to the next node
        print("None")  # Indicate the end of the list
s11 = SinglyLinkedList()
s11.insert(10)
s11.insert(20)
s11.insert(30)
s11.display()  # Display the linked list