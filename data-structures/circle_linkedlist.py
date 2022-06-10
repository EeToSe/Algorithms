class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        # hash set which stores h(node)
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

node1 = ListNode(1)
node2 = ListNode(2)
node1.next = node2
node2.next = node1

print(Solution().hasCycle(node1))