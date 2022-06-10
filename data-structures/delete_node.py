# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if (head.val == val):
            return head.next

        cur = head
        prev = None
        while (cur != None):
            if cur.val == val:
                prev.next = cur.next
            prev = cur
            cur = cur.next
        return head