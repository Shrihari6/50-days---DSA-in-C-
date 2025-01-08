'''Implement a basic stack using an array.'''

class Stack:
    def _init_(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from an empty stack")

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("peek from an empty stack")

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
