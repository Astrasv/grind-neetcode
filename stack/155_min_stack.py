class LinkedListNode:
    def __init__(self, val=None):
        self.val = val
        self.next = None

class MinStack:
    def __init__(self):
        self.head = None         
        self.min_head = None     

    def push(self, val: int) -> None:
        
        new_node = LinkedListNode(val)
        new_node.next = self.head
        self.head = new_node

        if not self.min_head or val <= self.min_head.val:
            min_node = LinkedListNode(val)
            min_node.next = self.min_head
            self.min_head = min_node

    def pop(self) -> None:
        if self.head:
            if self.head.val == self.min_head.val:
                self.min_head = self.min_head.next
            self.head = self.head.next

    def top(self) -> int:
        return self.head.val if self.head else None

    def getMin(self) -> int:
        return self.min_head.val if self.min_head else None
