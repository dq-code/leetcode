# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next==None:
            return head

        pilot = ListNode(0)
        pilot.next = head
        walker = pilot
        while walker.next != None and walker.next.next!=None:
            temp = walker.next.next
            walker.next.next = temp.next
            temp.next = walker.next
            walker.next = temp
            walker = walker.next.next

        return pilot.next