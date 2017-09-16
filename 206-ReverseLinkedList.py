# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None: return None
        pivot = ListNode(0)
        node = head
        while node:
            temp = node.next
            node.next = pivot.next
            pivot.next = node
            node = temp
        return pivot.next