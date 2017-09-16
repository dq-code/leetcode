# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        def reverse(node):
            pivot = ListNode(0)
            while node:
                temp = node.next
                node.next = pivot.next
                pivot.next = node
                node = temp
            return pivot.next

        l1 = reverse(l1)
        l2 = reverse(l2)

        res = ListNode(0)
        curNode = res
        residue = 0
        while l1 and l2:
            # print "l1 %d, l2 %d"%(l1.val, l2.val)
            curVal = l1.val + l2.val + residue
            curNode.next = ListNode(curVal % 10)
            residue = curVal / 10
            l1 = l1.next
            l2 = l2.next
            curNode = curNode.next

        while l1:
            # print "l1 %d"%(l1.val)
            curVal = l1.val + residue
            curNode.next = ListNode(curVal % 10)
            residue = curVal / 10
            l1 = l1.next
            curNode = curNode.next

        while l2:
            # print "l2 %d"%(l2.val)
            curVal = l2.val + residue
            curNode.next = ListNode(curVal % 10)
            residue = curVal / 10
            l2 = l2.next
            curNode = curNode.next

        # print residue
        if residue > 0:
            curNode.next = ListNode(residue)

        return reverse(res.next)
