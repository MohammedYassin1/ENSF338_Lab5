import random
import timeit
#1.
class MyArrayStack:
    def __init__(self):
        self._storage = []

    def push(self, value):
        self._storage.append(value)  # Append element at the tail

    def pop(self):
        if not self._storage:
            return None
        else:
            return self._storage.pop()  # Remove element from the tail

    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]

#2.
class ListNode:
    def __init__(self, value):
        self._value = value
        self._next = None

    def getData(self):
        return self._value

    def setData(self, value):
        self._value = value

    def getNext(self):
        return self._next

    def setNext(self, next):
        self._next = next

    def toString(self):
        return str(self._value)


class MyListStack:
    def __init__(self):
        self._head = None
    def push(self, value):
        node = ListNode(value)
        node.setNext(self._head)
        self._head = node
    def pop(self):
        if self._head is None:
            return None
        else:
            retval = self._head.getData()
            self._head = self._head.getNext()
            return retval
    def peek(self):
        if self._head is None:
            return None
        else:
            return self._head.getData()
        
'''
d = MyListStack()
for i in range(5):
    d.push(i)

for i in range(5):
    print(d.peek())
    print(d.pop())
'''
#3.
    
def generate_random_tasks():
    tasks = []
    probabilities = ['push', 'pop']
    probabilities_weights = [0.7, 0.3]  # Probability weights for push and pop

    for _ in range(10000):
        task_type = random.choices(probabilities, weights=probabilities_weights)[0]
        tasks.append(task_type)

    return tasks

#4.
lis = MyListStack()
arr = MyArrayStack()
lis_times = []
arr_times = []

random_tasks = generate_random_tasks()
i = 0
for j in random_tasks:
    i += 1
    print(i)
    if j == "push":
        lis_times.append(timeit.timeit(lambda: lis.push(2),number=100))
        arr_times.append(timeit.timeit(lambda: arr.push(2),number=100))
    elif j == "pop":
        lis_times.append(timeit.timeit(lambda: lis.pop(),number=100))
        arr_times.append(timeit.timeit(lambda: arr.pop(),number=100))
    else:
        print("error")

import matplotlib.pyplot as plt

# Plotting the distribution of times
plt.hist(lis_times, label='MyListStack', edgecolor='b', linewidth=1.5, width=0.00001, fill=False)
plt.hist(arr_times,  label='MyArrayStack', edgecolor='r', linewidth=1.5, width=0.00001, fill=False)
plt.xlim(0, 0.0001)  # Set the x-axis limits to zoom in
plt.xlabel('Time')
plt.ylabel('Frequency')
plt.title('Distribution of Times')
plt.legend()
plt.show()

#5.
'''
The graph shows how array implementation is faster than linked list implementation. This is shown by the higher frequency 
of the array implementation times in lower times. The array implementation is faster because it has an average constant time 
complexity, while the linked list implementation has an average linear time complexity because it lacks a tail pointer. This is
clearly shown by the graph as the array implementation has a higher frequency in lower times, while the linked list implementation
has a higher frequency in higher times.

'''






