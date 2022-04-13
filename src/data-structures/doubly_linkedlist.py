class LinkedList_Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

    # def later_node(self, i):
    #     if i == 0:
    #         return self
    #     if self.next is None:
    #         return -1
    #     else:
    #         return self.next.later_node(i - 1)


class MyLinkedList(object):

    def __init__(self):
        self.size = 0
        # Sentinel Node 伪结点
        self.head = LinkedList_Node(0)
        self.tail = LinkedList_Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1

        if (index + 1 < self.size - index):
            # iter from head
            current = self.head
            for _ in range(index + 1):
                current = current.next
        else:
            # iter from tail
            current = self.tail
            for _ in range(self.size - index):
                current = current.prev
        return current.val

    def addAtHead(self, val):
        prec, succ = self.head, self.head.next
        node = LinkedList_Node(val)
        self.size += 1
        node.prev = prec
        node.next = succ
        prec.next = node
        succ.prev = node

    def addAtTail(self, val):
        prec, succ = self.tail.prev, self.tail
        node = LinkedList_Node(val)
        self.size += 1
        node.prev = prec
        node.next = succ
        prec.next = node
        succ.prev = node

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        if index < 0:
            index = 0
        if index < self.size - index:
            prec = self.head
            for _ in range(index):
                prec = prec.next
            succ = prec.next
        else:
            succ = self.tail
            for _ in range(self.size - index):
                succ = succ.prev
            prec = succ.prev

        self.size += 1
        node = LinkedList_Node(val)
        node.prev = prec
        node.next = succ
        prec.next = node
        succ.prev = node

    def deleteAtIndex(self, index):
        if index >= 0 and index < self.size:
            if index < self.size - index:
                prec = self.head
                for _ in range(index):
                    prec = prec.next
                succ = prec.next.next
            else:
                succ = self.tail
                for _ in range(self.size - index - 1):
                    succ = succ.prev
                prec = succ.prev.prev
            self.size -= 1
            prec.next = succ
            succ.prev = prec

#Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(inde)
# print(param_1)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)