# Implement a Circular Queue
# Objective: Design a class `CircularQueue` that implements a circular queue with fixed size using a list.
# Parameters:
# - size: An integer representing the maximum number of elements the queue can hold.
# Returns:
# - None; methods handle the queue operations.
# Details:
# - Methods include `enqueue`, `dequeue`, `peek`, and `is_empty`.
# - `enqueue` should add an element to the queue if not full; otherwise, raise an exception.
# - `dequeue` should remove and return the element from the front if not empty; otherwise, raise an exception.
# - `peek` returns the front element without removing it.
# - `is_empty` checks whether the queue is empty.
# - Handle overflow and underflow appropriately with exceptions.

class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = -1
        self.rear = -1

    def enqueue(self, value):
        if (self.rear + 1) % self.size == self.front:
            raise Exception("Queue is full")
        elif self.front == -1: 
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = value
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = value

    def dequeue(self):
        if self.front == -1:
            raise Exception("Queue is empty")
        elif self.front == self.rear: 
            value = self.queue[self.front]
            self.front = -1
            self.rear = -1
        else:
            value = self.queue[self.front]
            self.front = (self.front + 1) % self.size
        return value

    def peek(self):
        if self.front == -1:
            raise Exception("Queue is empty")
        return self.queue[self.front]

    def is_empty(self):
        return self.front == -1

cq = CircularQueue(3)
cq.enqueue(1)
cq.enqueue(2)
print(cq.peek())  
print(cq.dequeue()) 
print(cq.is_empty())  
cq.enqueue(3)
cq.enqueue(4)
try:
    cq.enqueue(5)  
except Exception as e:
    print(e)  
print(cq.dequeue()) 
print(cq.dequeue())  
print(cq.is_empty())  


# Examples:
# cq = CircularQueue(3)
# cq.enqueue(1)
# cq.enqueue(2)
# print(cq.peek())  # Expected: 1
# print(cq.dequeue())  # Expected: 1
# print(cq.is_empty())  # Expected: False
# cq.enqueue(3)
# cq.enqueue(4)
# print(cq.dequeue())  # Expected: 2
# print(cq.dequeue())  # Expected: 3