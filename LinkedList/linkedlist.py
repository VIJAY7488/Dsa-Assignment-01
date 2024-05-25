class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0 or k == 0 or k % self.size == 0:
            return
        k = k % self.size
        current = self.head
        for _ in range(self.size - k - 1):
            current = current.next
        new_head = current.next
        current.next = None

        tail = new_head
        while tail.next:
            tail = tail.next
        tail.next = self.head
        self.head = new_head

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def merge(self, other):
        if self.head is None:
            self.head = other.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other.head
        self.size += other.size

    def interleave(self, other):
        p1 = self.head
        p2 = other.head
        while p1 and p2:
            p1_next = p1.next
            p2_next = p2.next

            p1.next = p2
            if p1_next is None:
                break

            p2.next = p1_next

            p1 = p1_next
            p2 = p2_next
        if p2:
            self.size += other.size - self.size // 2

    def get_middle(self):
        if self.size == 0:
            return None
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.value

    def index_of(self, value):
        current = self.head
        index = 0
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        if index == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            new_list.size = self.size
            self.head = None
            self.size = 0
            return self, new_list
        current = self.head
        for _ in range(index - 1):
            current = current.next
        new_list = SinglyLinkedList()
        new_list.head = current.next
        new_list.size = self.size - index
        current.next = None
        self.size = index
        return self, new_list