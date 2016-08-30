# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pos = 0
        pivot = ListNode(-1)
        pivot.next = head

        walker = pivot
        while pos < m:
            prev = walker
            walker = walker.next
            pos += 1

        walker_next = walker.next
        start = walker
        start_prev = prev
        while pos < n:
            temp = walker_next.next
            walker_next.next = walker
            walker = walker_next
            walker_next = temp
            pos += 1

        start_prev.next = walker
        start.next = walker_next

        return pivot.next
