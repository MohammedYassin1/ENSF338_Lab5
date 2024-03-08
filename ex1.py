import sys
#2. 
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

#3.
def evaluate(expression):
    stack = MyArrayStack()
    operators = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }

    for char in reversed(expression):
        if char in operators:
            intrermediate = operators[char](stack.pop(), stack.pop())
            stack.push(intrermediate)
        elif char not in '() ':
            stack.push(int(char))

    return stack.pop()

#1.
expression = sys.argv[1]
print(evaluate(expression))