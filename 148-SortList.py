# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeList(self, node1, node2):
        if node1 == None: return node2
        if node2 == None: return node1

        walker1 = node1
        walker2 = node2
        pivot = ListNode(0)
        walk = pivot
        while walker1 and walker2:
            if walker1.val < walker2.val:
                walk.next = walker1
                walker1 = walker1.next
            else:
                walk.next = walker2
                walker2 = walker2.next
            walk = walk.next
        if walker1:
            walk.next = walker1
        if walker2:
            walk.next = walker2
        return pivot.next

    def sortList(self, head):
        if head == None or head.next == None: return head
        fast = head
        slow = head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        head1 = head
        slow.next = None
        # print head1.val
        # print head2.val
        left = self.sortList(head1)
        right = self.sortList(head2)

        head = self.mergeList(left, right)
        return head
