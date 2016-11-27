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

        pivot = ListNode(0)
        walker = pivot
        res = 0
        while l1 and l2:
            #print "l1 value is %d"%l1.val
            #print "l2 value is %d"%l2.val
            sum = l1.val + l2.val + res
            res = sum/10
            val = sum%10
            newNode = ListNode(val)
            #print "newNode is %d"%newNode.val
            walker.next = newNode
            walker = walker.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                sum = l1.val + res
                res = sum/10
                val = sum%10
                newNode = ListNode(val)
                walker.next = newNode
                walker = walker.next
                l1 = l1.next
        elif l2:
            while l2:
                sum = l2.val + res
                res = sum/10
                val = sum%10
                newNode = ListNode(val)
                walker.next = newNode
                walker = walker.next
                l2 = l2.next
        if res>0:
            newNode = ListNode(res)
            walker.next = newNode


        return pivot.next
