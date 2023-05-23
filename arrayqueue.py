class ArrayQueue:
    def __init__(self, max_length=500):
        self.items = [None] * max_length
        self.front_idx = 0
        self.rear_idx = -1
        self.num_items = 0
        self.max_length = max_length

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def front(self):
        pass

    def is_empty(self):
        pass

    def is_full(self):
        pass
