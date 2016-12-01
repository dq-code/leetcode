# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} n
    # @return {ListNode}
    def removeNthFromEnd(self, head, n):
        if head == None:
            return None
        dummy = ListNode(0)
        dummy.next = head
        p1 = p2 = dummy
        count = n
        while count > 0:
            p1 = p1.next
            count = count - 1
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return dummy.next