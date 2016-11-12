# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
     def __init__(self, x):
         self.label = x
         self.next = None
         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        if head==None: return None

        map = {}
        copyHead = RandomListNode(head.label)
        map[head] = copyHead

        walker = head
        while walker!=None:
            if walker.next != None:
                if walker.next in map:
                    map[walker].next = map[walker.next]
                else:
                    copyNextNode = RandomListNode(walker.next.label)
                    map[walker].next = copyNextNode
                    map[walker.next] = copyNextNode
            if walker.random != None:
                if walker.random in map:
                    map[walker].random = map[walker.random]
                else:
                    copyRandomNode = RandomListNode(walker.random.label)
                    map[walker].random = copyRandomNode
                    map[walker.random] = copyRandomNode
            walker = walker.next

        return copyHead



