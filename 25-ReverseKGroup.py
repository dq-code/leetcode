# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None
        if k <= 1: return head
        pivot = ListNode(0)
        pivot.next = head
        start = pivot
        walker = pivot.next
        count = 1
        while walker and walker.next:
            newHead = walker.next
            walker.next = newHead.next
            newHead.next = start.next
            start.next = newHead
            count += 1
            if count == k:
                count = 1
                start = walker
                walker = walker.next

        if count != 1:
            walker = start.next
            while walker.next:
                newHead = walker.next
                walker.next = newHead.next
                newHead.next = start.next
                start.next = newHead

        return pivot.next
