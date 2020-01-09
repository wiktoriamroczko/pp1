class Queue():
    
    def __init__(self):
        self.queue = []
        
    def pop(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def push(self, item):
        self.queue.append(item)

    def is_empty(self):
        return len(self.queue)==0
    
s = Queue()
s.push(2)
s.push(5)
s.push(9)
s.push(1)
s.push(3)
for i in range(3):
    print(s.pop())