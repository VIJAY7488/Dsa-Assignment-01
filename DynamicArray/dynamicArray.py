class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        self.array.insert(index, value)
        self.size += 1
        self._resize_if_needed()

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        self.array.pop(index)
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0 or k == 0 or k % self.size == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        self.array = self.array[::-1]

    def append(self, value):
        self.array.append(value)
        self.size += 1
        self._resize_if_needed()

    def prepend(self, value):
        self.array.insert(0, value)
        self.size += 1
        self._resize_if_needed()

    def merge(self, other):
        self.array.extend(other.array)
        self.size += other.size
        self._resize_if_needed()

    def interleave(self, other):
        new_array = []
        i, j = 0, 0
        while i < self.size and j < other.size:
            new_array.append(self.array[i])
            new_array.append(other.array[j])
            i += 1
            j += 1
        while i < self.size:
            new_array.append(self.array[i])
            i += 1
        while j < other.size:
            new_array.append(other.array[j])
            j += 1
        self.array = new_array
        self.size = len(new_array)

    def get_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, value):
        for i in range(self.size):
            if self.array[i] == value:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        left_array = DynamicArray(self.resize_factor)
        right_array = DynamicArray(self.resize_factor)
        left_array.array = self.array[:index]
        left_array.size = index
        right_array.array = self.array[index:]
        right_array.size = self.size - index
        return left_array, right_array

    def _resize_if_needed(self):
        if len(self.array) > self.size * self.resize_factor:
            self.array = self.array[:self.size]