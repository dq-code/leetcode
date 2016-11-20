# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None: return head

        pivot = ListNode(0)
        pivot.next = head

        walker = head.next
        prev = head
        while walker:
            if prev.val > walker.val:
                temp = walker.next
                comp = pivot.next
                compPrev = pivot
                while comp != walker:
                    if comp.val > walker.val:
                        # print "walker val %d"%walker.val
                        # print "comp val %d"%comp.val
                        compPrev.next = walker
                        walker.next = comp
                        prev.next = temp
                        break
                    compPrev = comp
                    comp = comp.next
                if comp == walker:
                    prev = walker
                walker = temp
            else:
                prev = walker
                walker = walker.next
        return pivot.next
