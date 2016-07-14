# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def __init__(self):
        self.heapList = []

    def addToHeap(self, node):
        self.heapList.append(node)
        curIndex = len(self.heapList) - 1
        while curIndex > 0:
            curParentIndex = (curIndex + 1) / 2 - 1
            if self.heapList[curIndex].val < self.heapList[curParentIndex].val:
                self.heapList[curIndex], self.heapList[curParentIndex] = self.heapList[curParentIndex], \
                                                                         self.heapList[curIndex]
                curIndex = curParentIndex
            else:
                break
        return curIndex

    def removeFromHeap(self):
        removedNode = self.heapList[0]
        if len(self.heapList) > 1:
            self.heapList[0] = self.heapList.pop()
            curIndex = 0
            while curIndex < len(self.heapList) - 1:
                leftChildIndex = curIndex * 2 + 1
                rightChildIndex = curIndex * 2 + 2
                if leftChildIndex >= len(self.heapList):
                    break
                childIndex = leftChildIndex
                if rightChildIndex < len(self.heapList) and self.heapList[leftChildIndex].val > self.heapList[
                    rightChildIndex].val:
                    childIndex = rightChildIndex
                if self.heapList[curIndex].val > self.heapList[childIndex].val:
                    self.heapList[curIndex], self.heapList[childIndex] = self.heapList[childIndex], \
                                                                         self.heapList[curIndex]
                    curIndex = childIndex
                else:
                    break
        else:
            self.heapList.pop()

        return removedNode

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return None

        for i in range(len(lists)):
            if lists[i] != None:
                self.addToHeap(lists[i])
        if len(self.heapList) == 0:
            return None
        head = self.removeFromHeap()
        walker = head
        while len(self.heapList) > 0:
            nodeToAdd = walker.next
            while nodeToAdd != None:
                index = self.addToHeap(nodeToAdd)
                if index == 0:
                    res = self.removeFromHeap()
                    walker.next = res
                    walker = walker.next
                    nodeToAdd = res.next
                else:
                    break

            res = self.removeFromHeap()
            walker.next = res
            walker = walker.next

        return head
