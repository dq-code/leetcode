# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head==None or head.next==None:
            return

        fast = head.next
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        walker = slow.next
        prev = None
        while walker:
            temp = walker.next
            walker.next = prev
            prev = walker
            walker = temp

        walker1 = head
        walker2 = prev

        while walker1 and walker2:
            temp1 = walker1.next
            temp2 = walker2.next
            walker1.next = walker2
            walker2.next = temp1
            walker1 = temp1
            walker2 = temp2

