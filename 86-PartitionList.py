# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        pivot = ListNode(0)
        pivot.next = head

        partition = pivot
        walker = pivot

        while walker.next:
            if walker.next.val < x:
                if partition == walker:
                    # print "partition same as walker"
                    partition = walker.next
                    walker = walker.next
                else:
                    # print "partition diff from walker"
                    temp_walker_next = walker.next
                    walker.next = temp_walker_next.next
                    temp_par_next = partition.next
                    partition.next = temp_walker_next
                    temp_walker_next.next = temp_par_next
                    partition = partition.next
            else:
                walker = walker.next

        return pivot.next
