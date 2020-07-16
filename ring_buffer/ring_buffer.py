class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.oldest = 0

    def append(self, item):
        if self.capacity == len(self.storage):
            # replace the head or the oldest
            self.storage[self.oldest] = item
            self.oldest += 1 # increments oldest starting at 1
            self.oldest %= self.capacity # when oldest hits 3 it will revert to 0
        else:
            self.storage.append(item)

    def get(self):
        return self.storage

# start sprint at 3pm EST 7/16/2020
"""
buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

buffer.get()   # should return ['a', 'b', 'c']

# 'd' overwrites the oldest value in the ring buffer, which is 'a'
buffer.append('d')

buffer.get()   # should return ['d', 'b', 'c']

buffer.append('e')
buffer.append('f')

buffer.get()   # should return ['d', 'e', 'f']
"""