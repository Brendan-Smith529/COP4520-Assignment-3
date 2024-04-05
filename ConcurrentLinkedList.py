import threading

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ConcurrentLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lock = threading.Lock()

    def append(self, data):
        new_node = Node(data)

        with self.lock:
            if not self.head:
                self.head = new_node
                self.tail = new_node
                return

            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove(self):
        with self.lock:
            if not self.head:
                return

            elif self.head == self.tail:
                self.head = None
                self.tail = None

            else:
                self.head = self.head.next

    def search(self, data):
        with self.lock:
            if not self.head:
                return

            current_node = self.head
            while current_node.next and current_node.data != data:
                current_node = current_node.next

            return current_node if current_node else None
