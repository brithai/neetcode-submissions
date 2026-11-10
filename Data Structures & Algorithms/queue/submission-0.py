class ListNode():
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)

        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.tail
        new_node.prev = self.tail.prev

        self.tail.prev.next = new_node
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = ListNode(value)
        new_node.next = self.head.next
        new_node.prev = self.head

        self.head.next.prev = new_node
        self.head.next = new_node

    def pop(self) -> int:
        if self.tail.prev == self.head:
            return -1

        val = self.tail.prev.val

        self.tail.prev.prev.next = self.tail
        self.tail.prev = self.tail.prev.prev

        return val

    def popleft(self) -> int:
        if self.head.next == self.tail:
            return -1

        val = self.head.next.val

        self.head.next.next.prev = self.head
        self.head.next = self.head.next.next

        return val
        
