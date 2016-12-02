# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return None

        heap = []
        pivot = ListNode(0)
        walker = pivot

        def addIntoHeap(node):
            heap.append(node)
            index = len(heap) - 1
            while index > 0:
                parent = (index + 1) / 2 - 1
                if heap[parent].val <= heap[index].val:
                    break
                heap[parent], heap[index] = heap[index], heap[parent]
                index = parent

        def popFirstFromHeap():
            top = heap[0]
            newTop = heap[-1]
            heap.pop()
            if len(heap) == 0: return top
            heap[0] = newTop
            index = 0
            while index < len(heap):
                left = index * 2 + 1
                if left >= len(heap): break
                minChild = left
                right = index * 2 + 2
                if right < len(heap) and heap[left].val > heap[right].val:
                    minChild = right
                if heap[minChild].val < heap[index].val:
                    heap[index], heap[minChild] = heap[minChild], heap[index]
                    index = minChild
                else:
                    break
            return top

        for i in range(len(lists)):
            if lists[i]:
                addIntoHeap(lists[i])

        while len(heap) > 0:
            node = popFirstFromHeap()
            # print node.val
            if node.next:
                addIntoHeap(node.next)
            walker.next = node
            walker = walker.next

        return pivot.next
