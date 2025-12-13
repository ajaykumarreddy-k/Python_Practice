# Stack Data Structure Implementation

class Stack:
    def __init__(self):
            # The stack is implemented using a Python list.
        self.items = []

    def push(self, item):
        # Adds a new item to the top of the stack.
        # The append method of list adds the item to the end, simulating the top of the stack.
        self.items.append(item)

    def pop(self):
        # Removes and returns the item from the top of the stack.
        # Checks if the stack is empty before popping to prevent errors.
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        # Returns the item at the top of the stack without removing it.
        # Checks if the stack is empty before peeking.
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty"

    def is_empty(self):
        # Checks if the stack is empty.
        # Returns True if the stack contains no elements, False otherwise.
        return len(self.items) == 0

    def size(self):
        # Returns the number of items currently in the stack.
        return len(self.items)


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
my_stack.push(40)
my_stack.push(50)
print("Stack after pushes:", my_stack.items)
print("Top element (peek):", my_stack.peek())
print("Popped element:", my_stack.pop())
print("Stack after one pop:", my_stack.items)
print("Is stack empty?", my_stack.is_empty())
print("Stack size:", my_stack.size())
# we dont push two elements at a time, we push one by one.
# we can pop one by one, we can peek the top element, we can check if the stack is empty, and we can check the size of the stack.
# we can also print the stack after each operation to see the changes.