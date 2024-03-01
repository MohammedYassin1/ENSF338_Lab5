import random
import timeit
#1.
class MyArrayStack:
    def __init__(self):
        self._storage = []

    def push(self, value):
        self._storage.append(value)

    def pop(self):
        if not self._storage:
            return None
        else:
            return self._storage.pop(-1)  # Changed to pop the last element

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
for i in range(100):
    random_tasks = generate_random_tasks()
    for j in random_tasks:
        if j == "push":
            lis_times.append(timeit.timeit(lambda: lis.push(2),number=1))
            arr_times.append(timeit.timeit(lambda: arr.push(2),number=1))
        elif j == "pop":
            lis_times.append(timeit.timeit(lambda: lis.pop(),number=1))
            arr_times.append(timeit.timeit(lambda: arr.pop(),number=1))

def test_stack_performance():
    for _ in range(100):
        tasks = generate_random_tasks()
        stack = MyListStack()
        for task in tasks:
            if task == 'push':
                stack.push(1)
            elif task == 'pop':
                stack.pop()





