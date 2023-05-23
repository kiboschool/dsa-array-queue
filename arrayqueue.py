class ArrayQueue:
    def __init__(self, max_length=500):
        self.items = [None] * max_length
        self.front_idx = 0
        self.rear_idx = -1
        self.num_items = 0
        self.max_length = max_length

    def enqueue(self, item):
        if self.is_full():
            return False

        self.rear_idx = (self.rear_idx + 1) % self.max_length
        self.items[self.rear_idx] = item
        self.num_items += 1
        return True

    def dequeue(self):
        if self.is_empty():
            return None

        removed = self.items[self.front_idx]
        self.front_idx = (self.front_idx + 1) % self.max_length
        self.num_items -= 1
        return removed

    def front(self):
        return self.items[self.front_idx]

    def is_empty(self):
        return self.num_items == 0

    def is_full(self):
        return self.num_items == self.max_length
