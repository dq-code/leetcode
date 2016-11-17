# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return None

        fast = slow = head

        loop = False
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                loop = True
                break

        if not loop: return None

        slow = head
        while fast != slow:
            fast = fast.next
            slow = slow.next

        return fast
