class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
    
s = Stack()
s.push(2)
s.push(5)
s.push(9)
s.push(1)
s.push(3)
for i in range(3):
    print(s.pop())