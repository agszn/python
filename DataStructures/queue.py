from collections import deque

class Queue:
    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.popleft()

    def peek(self):
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

# Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())  # 1
queue.dequeue()
print(queue.peek())  # 2
