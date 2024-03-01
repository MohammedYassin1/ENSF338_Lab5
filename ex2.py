#1.
class PriorityArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.priorities = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        self.priorities[self.tail] = priority
        self._sort_by_priority()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Unable to peek item.")
            return None
        return self.queue[self.head]




#2.
class PriorityArrayQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.priorities = [None] * capacity
        self.head = -1
        self.tail = -1

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head

    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue[self.tail] = item
        self.priorities[self.tail] = priority
        self._sort_by_priority()

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Unable to dequeue item.")
            return None
        item = self.queue[self.head]
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
        else:
            self.head = (self.head + 1) % self.capacity
        return item

    def peek(self):
        if self.is_empty():
            print("Queue is empty. Unable to peek item.")
            return None
        return self.queue[self.head]


