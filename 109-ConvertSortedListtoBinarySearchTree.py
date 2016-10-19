# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None: return None

        slow = fast = head
        prev = None
        while fast:
            if fast.next:
                fast = fast.next
            else:
                break
            if fast.next:
                fast = fast.next
            else:
                break
            prev = slow
            slow = slow.next
        if prev:
            prev.next = None

        root = TreeNode(slow.val)
        if slow != head:
            root.left = self.sortedListToBST(head)
        else:
            root.left = None
        root.right = self.sortedListToBST(slow.next)

        return root
