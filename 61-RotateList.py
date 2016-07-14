# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None: return None

        pivot = ListNode(0)
        pivot.next = head

        count = 0
        walker = pivot.next
        while walker:
            count += 1
            walker = walker.next

        new_k = k % count
        if new_k == 0: return head

        walker = pivot.next
        node_list = []
        while walker:
            if len(node_list) >= new_k+1:
                node_list.pop(0)
            node_list.append(walker)
            walker = walker.next
        while len(node_list) > 1:
            new_head = node_list.pop()
            temp = pivot.next
            pivot.next = new_head
            new_head.next = temp

        node_list.pop().next = None

        return pivot.next
