import sys

class MyArrayStack:
    def __init__(self):
        self._storage = []
    def push(self, value):
        self._storage.append(value)
    def pop(self):
        # Note that in Python "not <list>" evaluates to True if the list is empty
        if not self._storage:
            return None
        else:
            return self._storage.pop()
    def peek(self):
        if not self._storage:
            return None
        else:
            return self._storage[-1]

def evaluate(expression):
    stack = MyArrayStack()
    operators = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: x / y
    }

    for char in reversed(expression):
        if char in operators:
            stack.push(operators[char](stack.pop(), stack.pop()))
        elif char not in '() ':
            stack.push(int(char))

    return stack.pop()

expression = sys.argv[1]
print(evaluate(expression))



    