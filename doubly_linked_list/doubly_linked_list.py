from typing import Optional
from unittest.loader import defaultTestLoader

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev: Optional[ListNode] = prev
        self.next: Optional[ListNode] = next

    def insert_after(self, value):
        current_next = self.next
        node = ListNode(value, self, current_next)
        self.next = node
        if current_next:
            current_next.prev = self.next
        return node

    def insert_before(self, value):
        current_prev = self.prev
        node = ListNode(value, current_prev, self)
        self.prev = node
        if current_prev:
            current_prev.next = self.prev
        return node

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def remove_from_head(self):
        if self.head is None:
            return None
        data = self.head.value
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.delete(self.head)
        self.length -= 1
        return data

    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        if not self.head and not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def remove_from_tail(self):
        if self.tail is None:
            return None
        data = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.delete(self.tail)
        self.length -= 1
        return data

    def move_to_front(self, node):
        value = node.value
        self.delete(node)
        self.add_to_head(value)

    def move_to_end(self, node):
        value = node.value
        self.delete(node)
        self.add_to_tail(value)

    def delete(self, node):
        if not self.head:

            return None
        if self.head == self.tail:
            self.head = None
            self.tail = None
        if node == self.head:
            self.head = node.next
            node.delete()
        if node == self.tail:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()
        self.length -= 1

    """Returns the highest value currently in the list"""
    def get_max(self):
        max = 0
        current = self.head
        while current is not None:
            if current.value > max:
                max = current.value
            current = current.next
        return max