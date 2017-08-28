# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Related to find start point of cycled linked list
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """

        if not headA or not headB:
            return None
        walker = headA
        while walker.next!=None:
            walker=walker.next
        walker.next=headB

        fast = slow = headA
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        if not fast or not fast.next:
            walker.next = None
            return None
        fast = headA
        while fast!=slow:
            fast = fast.next
            slow = slow.next
        walker.next = None
        return fast
