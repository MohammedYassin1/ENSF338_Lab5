# Exercise 4
# Question 1
class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # Insert an element at the head (index 0)
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            # Remove an element from the tail (last index)
            return self.queue.pop()
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

# Example usage:
queue = ArrayQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue:", queue.queue)
print("Dequeue:", queue.dequeue())
print("Queue:", queue.queue)
print("Is Empty:", queue.is_empty())
print("Size:", queue.size())




# Question 2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            current = self.head
            prev = None

            # Traverse to the tail of the list
            while current.next is not None:
                prev = current
                current = current.next

            # Update tail and dequeue the element
            if prev is not None:
                prev.next = None
                self.tail = prev
            else:
                # If there's only one element
                self.head = None
                self.tail = None

            return current.data
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

# Example usage:
linked_list_queue = LinkedListQueue()
linked_list_queue.enqueue(1)
linked_list_queue.enqueue(2)
linked_list_queue.enqueue(3)

print("Queue size:", linked_list_queue.size())
print("Dequeue:", linked_list_queue.dequeue())
print("Queue size:", linked_list_queue.size())
print("Is Empty:", linked_list_queue.is_empty())




# Question 3
import random

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        # Generate a random number between 0 and 1
        probability = random.random()

        # Enqueue with probability 0.7
        if probability < 0.7:
            tasks.append("enqueue")
        # Dequeue with probability 0.3
        else:
            tasks.append("dequeue")

    return tasks

# Example usage:
random_tasks = generate_random_tasks()
print(random_tasks[:10])  # Print the first 10 tasks as an example





# Question 4
import timeit
import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            current = self.head
            prev = None

            while current.next is not None:
                prev = current
                current = current.next

            if prev is not None:
                prev.next = None
                self.tail = prev
            else:
                self.head = None
                self.tail = None

            return current.data
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        probability = random.random()
        if probability < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

def run_test(queue, tasks):
    for task in tasks:
        if task == "enqueue":
            queue.enqueue(1)
        elif task == "dequeue":
            queue.dequeue()

# Generate 100 lists of tasks
lists_of_tasks = [generate_random_tasks() for _ in range(100)]

# Measure the performance of the array-based queue
array_queue_time = timeit.timeit(lambda: run_test(ArrayQueue(), lists_of_tasks[0]), number=1)
print("Array Queue Time:", array_queue_time)

# Measure the performance of the linked list-based queue
linked_list_queue_time = timeit.timeit(lambda: run_test(LinkedListQueue(), lists_of_tasks[0]), number=1)
print("Linked List Queue Time:", linked_list_queue_time)






# Question 5
import timeit
import random
import matplotlib.pyplot as plt

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def dequeue(self):
        if not self.is_empty():
            current = self.head
            prev = None

            while current.next is not None:
                prev = current
                current = current.next

            if prev is not None:
                prev.next = None
                self.tail = prev
            else:
                self.head = None
                self.tail = None

            return current.data
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return self.head is None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

class ArrayQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.insert(0, item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            print("Queue is empty. Cannot dequeue.")

    def is_empty(self):
        return len(self.queue) == 0

    def size(self):
        return len(self.queue)

def generate_random_tasks():
    tasks = []
    for _ in range(10000):
        probability = random.random()
        if probability < 0.7:
            tasks.append("enqueue")
        else:
            tasks.append("dequeue")
    return tasks

def run_test(queue, tasks):
    for task in tasks:
        if task == "enqueue":
            queue.enqueue(1)
        elif task == "dequeue":
            queue.dequeue()

# Generate 100 lists of tasks
lists_of_tasks = [generate_random_tasks() for _ in range(100)]

# Measure the performance of the array-based queue
array_queue_times = [timeit.timeit(lambda: run_test(ArrayQueue(), tasks), number=1) for tasks in lists_of_tasks]

# Measure the performance of the linked list-based queue
linked_list_queue_times = [timeit.timeit(lambda: run_test(LinkedListQueue(), tasks), number=1) for tasks in lists_of_tasks]

# Plotting the distribution of times
plt.hist(array_queue_times, bins=20, alpha=0.5, label='Array Queue')
plt.hist(linked_list_queue_times, bins=20, alpha=0.5, label='Linked List Queue')
plt.xlabel('Time (seconds)')
plt.ylabel('Frequency')
plt.legend()
plt.title('Distribution of Queue Operation Times')
plt.show()
