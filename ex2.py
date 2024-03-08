#1.
class PriorityQueue:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.head = -1
        self.tail = -1


    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.queue.append((item, priority))
        self.queue = self.merge_sort(self.queue)


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
        return item[0]

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head
    
    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left_half = self.merge_sort(arr[:mid])
        right_half = self.merge_sort(arr[mid:])
        return self.merge(left_half, right_half)

    def merge(self, left_half, right_half):
        merged = []
        while left_half and right_half:
            if left_half[0][1] < right_half[0][1]:
                merged.append(left_half.pop(0))
            else:
                merged.append(right_half.pop(0))
        merged.extend(left_half if left_half else right_half)
        return merged

#2.
class PriorityQueue2:
    def __init__(self, capacity):
        self.queue = []
        self.capacity = capacity
        self.head = -1
        self.tail = -1


    def enqueue(self, item, priority):
        if self.is_full():
            print("Queue is full. Unable to enqueue item.")
            return
        elif self.is_empty():
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.capacity
        self.insert_item((item, priority))


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
        return item[0]

    def is_empty(self):
        return self.head == -1

    def is_full(self):
        return (self.tail + 1) % self.capacity == self.head
    
    def insert_item(self, item):
        if self.is_empty():
            self.queue.append(item)
            self.head = 0
            self.tail = 0
        else:
            for i in range(len(self.queue)):
                if self.queue[i][1] > item[1]:
                    self.queue.insert(i, item)
                    return
            self.queue.append(item)

prior = PriorityQueue2(5)           
prior.enqueue(1, 3)
prior.enqueue(2, 1)
prior.enqueue(3, 2)
prior.enqueue(4, 5)
prior.enqueue(5, 4)
print(prior.queue)
print(prior.dequeue())
print(prior.dequeue())
print(prior.dequeue())
print(prior.dequeue())
print(prior.dequeue())
print(prior.dequeue())

#3.
import random
import timeit

def generate_random_tasks():
    tasks = []
    probabilities = ['enqueue', 'dequeue']
    probabilities_weights = [0.7, 0.3] 

    for _ in range(1000):
        task_type = random.choices(probabilities, weights=probabilities_weights)[0]
        tasks.append(task_type)

    return tasks

#4.

sort = PriorityQueue(700)
search = PriorityQueue2(700)
lis_times = []
arr_times = []

random_tasks = generate_random_tasks()
i = 0
for j in random_tasks:
    i += 1
    print(i)
    if j == "enqueue":
        lis_times.append(timeit.timeit(lambda: sort.enqueue(2, random.randint(0,100)),number=100))
        arr_times.append(timeit.timeit(lambda: search.enqueue(2, random.randint(0,100)),number=100))
    elif j == "dequeue":
        lis_times.append(timeit.timeit(lambda: sort.dequeue(),number=100))
        arr_times.append(timeit.timeit(lambda: search.dequeue(),number=100))
    else:
        print("Invalid task")


print("Average time for Sort: ",lis_times)
print("Average time for search: ",arr_times)

print("Average time for Sort: ", sum(lis_times) / len(lis_times))
print("Average time for search: ", sum(arr_times) / len(arr_times))

#5.
'''
The PriorityQueue2 class is faster than the PriorityQueue class. This is because the PriorityQueue2 class uses linear search
to find the right position to insert the item, which has an average complexity of O(n).While  PriorityQueue class uses merge_sort 
method which has a time complexity of O(nlogn). While PriorityQueue could be faster for smaller Priority Queue sizes, because we
tested the performance of the two classes with a PriorityQueue size of 700, the PriorityQueue2 class was faster.
'''