# Exercise 5
# Question 1
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, element):
        if self.is_full():
            print("enqueue None")
            return

        if self.is_empty():
            self.front = self.rear = 0
        else:
            self.rear = (self.rear + 1) % self.capacity

        self.queue[self.rear] = element
        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None

        element = self.queue[self.front]

        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity

        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None

        element = self.queue[self.front]
        print(f"peek {element}")
        return element


# Example usage:
cq = CircularQueue(5)

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

cq.peek()

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.peek()

cq.dequeue()  # Trying to dequeue from an empty queue
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)  # Trying to enqueue into a full queue




# Question 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None

        element = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None

        element = self.front.data
        print(f"peek {element}")
        return element


# Example usage:
cq = CircularQueue()

cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)

cq.peek()

cq.dequeue()
cq.dequeue()
cq.dequeue()

cq.peek()

cq.dequeue()  # Trying to dequeue from an empty queue
cq.enqueue(4)
cq.enqueue(5)
cq.enqueue(6)  # Circular linked list will handle enqueueing beyond the initial capacity






# Question 3
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, element):
        new_node = Node(element)

        if self.is_empty():
            self.front = self.rear = new_node
            self.rear.next = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.rear.next = self.front

        print(f"enqueue {element}")

    def dequeue(self):
        if self.is_empty():
            print("dequeue None")
            return None

        element = self.front.data

        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.rear.next = self.front

        print(f"dequeue {element}")
        return element

    def peek(self):
        if self.is_empty():
            print("peek None")
            return None

        element = self.front.data
        print(f"peek {element}")
        return element


# Example usage:
cq = CircularQueue()

# Enqueue operations
cq.enqueue(1)  # enqueue 1
cq.enqueue(2)  # enqueue 2
cq.enqueue(3)  # enqueue 3
cq.enqueue(4)  # enqueue 4

# Peek operations
cq.peek()       # peek 1

# Dequeue operations
cq.dequeue()    # dequeue 1
cq.dequeue()    # dequeue 2

# Enqueue to full queue
cq.enqueue(5)   # enqueue 5
cq.enqueue(6)   # enqueue 6
cq.enqueue(7)   # enqueue 7
cq.enqueue(8)   # enqueue 8

# Peek into empty queue
cq.dequeue()    # dequeue 3
cq.peek()       # peek None

# Enqueue into full queue
cq.enqueue(9)   # enqueue None

# More regular operations
cq.enqueue(10)  # enqueue 10
cq.peek()       # peek 4
cq.dequeue()    # dequeue 4

# Continue operations
cq.enqueue(11)  # enqueue 11
cq.enqueue(12)  # enqueue 12
cq.enqueue(13)  # enqueue 13

# Dequeue and Peek
cq.dequeue()    # dequeue 5
cq.peek()       # peek 6

# Dequeue all remaining elements
cq.dequeue()    # dequeue 6
cq.dequeue()    # dequeue 7
cq.dequeue()    # dequeue 8
cq.dequeue()    # dequeue 9

# Attempt to dequeue from an empty queue
cq.dequeue()    # dequeue None

# Enqueue into empty queue
cq.enqueue(14)  # enqueue 14

# Peek into non-empty queue
cq.peek()       # peek 14


"""
Expected Outputs
enqueue 1
enqueue 2
enqueue 3
enqueue 4
peek 1
dequeue 1
dequeue 2
enqueue 5
enqueue 6
enqueue 7
enqueue 8
dequeue 3
peek 4
enqueue 9
enqueue 10
peek 4
dequeue 4
enqueue 11
enqueue 12
enqueue 13
dequeue 5
peek 6
dequeue 6
dequeue 7
dequeue 8
dequeue 9
dequeue 10
enqueue 14
peek 11
11
"""