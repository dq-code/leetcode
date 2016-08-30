# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head

        pivot = ListNode('x')
        pivot.next = head

        prev = head
        node = head.next
        start = pivot

        while node:
            if node.val == prev.val:
                dup_val = node.val
                temp = start.next
                # print start.val
                while temp and temp.val == dup_val:
                    # print temp.val
                    temp = temp.next
                start.next = temp
                if not temp: break
                prev = temp
                node = temp.next
            else:
                start = prev
                prev = node
                node = node.next

        return pivot.next
