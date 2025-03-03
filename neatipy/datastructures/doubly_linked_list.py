from .node import Node


class DoublyLinkedList:
    def __init__(self) -> None:
        self.size = 0
        self.head = None
        self.tail = None

    def is_empty(self) -> bool:
        """Checks if DLL is empty"""
        return self.head is None

    def remove_from_tail(self) -> None:
        """Remove from tail"""
        if self.is_empty():
            return
        new_tail = self.tail.prev
        if new_tail is None:
            self.head = None
            self.tail = None
            self.size -= 1
            return
        self.tail = new_tail
        self.tail.next = None
        self.size -= 1

    def remove(self, node: Node) -> None:
        """Remove node from list, assumes it exists. In this context we will check its existence using hashmap as this class will be used in LRU cache"""
        if self.is_empty():
            return
        if self.tail is node:
            self.tail = node.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        elif self.head is node:
            self.head = node.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.size -= 1

    def insert_to_head(self, node: Node) -> None:
        """Insert node to head"""
        if self.is_empty():
            self.head = node
            self.head.prev = None
            self.head.next = None
            self.tail = self.head
            self.size += 1
            return
        old_head = self.head
        old_head.prev = node
        self.head = node
        self.head.next = old_head
        self.head.prev = None
        self.size += 1
