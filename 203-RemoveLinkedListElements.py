# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        if head == None: return head
        pivot = ListNode(0)
        pivot.next = head
        prev = pivot
        while prev and prev.next:
            # print prev.val
            if prev.next.val == val:
                prev.next = prev.next.next
            else:
                prev = prev.next
        return pivot.next
