# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def mergeTwoLists(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        n1 = l1
        n2 = l2
        dummy = ListNode(0)
        node = dummy
        while n1 and n2:
            if n1.val <= n2.val:
                node.next = n1
                n1 = n1.next
            else:
                node.next = n2
                n2 = n2.next
            node = node.next
        if n1:
            node.next = n1
        elif n2:
            node.next = n2
        return dummy.next
