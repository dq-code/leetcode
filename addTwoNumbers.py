# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        head = prev = ListNode(0)
        node1 = l1
        node2 = l2
        extra = 0
        while node1 or node2:
            val1 = node1.val if node1 else 0
            if node1:   
                node1 = node1.naxt
            val2 = node2.val if node2 else 0
            if node2:
                node2 = node2.next
            sum = val1 + val2 + extra
            extra = int(sum/10)
            value = int(sum%10)
            prev.next = ListNode(value)
            prev = prev.next
        if extra>0:
            prev.next = ListNode(extra)
        return head.next