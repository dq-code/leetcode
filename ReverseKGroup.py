# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def checkIfEnoughNodeLeft(self, start, count):
        node = start
        while node and count > 1:
            count = count - 1
            node = node.next
        if count == 1: return node
        return None

    def reverseThisGroup(self, start, count):
        node = start
        orig_next_node = start.next
        while node != None and orig_next_node != None and count > 1:
            temp = orig_next_node.next
            orig_next_node.next = node
            node = orig_next_node
            orig_next_node = temp
            count = count - 1
        start.next = orig_next_node

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None

        pilot = ListNode(-1)
        pilot.next = head
        walker = pilot
        while walker.next:
            group_head = walker.next
            tail = self.checkIfEnoughNodeLeft(group_head, k)
            if tail == None:
                break
            walker.next = tail
            self.reverseThisGroup(group_head, k)
            walker = group_head

        return pilot.next
