# Queue Data Structure Implementation
class Queue():
    def __init__(self):
        # Initialize an empty list to store queue items.
        self.item = []

    def enqueue(self,item):
        # Add an item to the end of the queue.
        self.item.append(item)
        print(item,"added to the queue")

    def dequeue(self):
        # Remove and return the item from the front of the queue.
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.item.pop(0)

    def is_empty(self):
        # Check if the queue is empty.
        return len(self.item) == 0

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
print("Queue after enqueues:", q.item)
print("Dequeued element:", q.dequeue())
print("Queue after one dequeue:", q.item)
print("Is queue empty?", q.is_empty())      
# Deque is in notion -> placement notes and zaara colab check it out 


'''class Deque():
    def __init__(self):
        self.items = []
    def add_front(self, item):
        # Add an item to the front of the deque.
        self.items.insert(0, item)
    def add_rear(self, item):
        # Add an item to the rear of the deque.
        self.items.append(item)
    def remove_front(self):
        # Remove and return the item from the front of the deque.
        if not self.is_empty():
            return self.items.pop(0)
        return "Deque is empty"
    def remove_rear(self):
        # Remove and return the item from the rear of the deque.
        if not self.is_empty():
            return self.items.pop()
        return "Deque is empty"     
dq = Deque()
dq.add_front(10)
dq.add_rear(20)
dq.add_front(30)
print("Deque after additions:", dq.items)
print("Removed from front:", dq.remove_front())
print("Removed from rear:", dq.remove_rear())
print("Deque after removals:", dq.items)
'''