# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head==None or head.next==None: return True
        slow = fast = head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            slow = slow.next


        pivot = ListNode(0)
        node = slow
        while node:
            temp = node.next
            node.next = pivot.next
            pivot.next = node
            node = temp

        node1 = head
        node2 = pivot.next

        while node2:
            if node1.val!=node2.val:
                return False
            node1 = node1.next
            node2 = node2.next

        return True
