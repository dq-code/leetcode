class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.tail.prev = self.head
        self.head.next = self.tail

    def remove(self, node):
        tempPrev = node.prev
        tempNext = node.next
        tempPrev.next = tempNext
        tempNext.prev = tempPrev

    def addFirst(self, node):
        curHead = self.head.next
        self.head.next = node
        node.next = curHead
        curHead.prev = node
        node.prev = self.head

    def removeLast(self):
        curTail = self.tail.prev
        curTailPrev = curTail.prev
        curTailPrev.next = self.tail
        self.tail.prev = curTailPrev
        return curTail


class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cache = DoubleLinkedList()
        self.map = {}
        self.capacity = capacity

    def isFull(self):
        return len(self.map) >= self.capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.map:
            self.cache.remove(self.map[key])
            self.cache.addFirst(self.map[key])
            return self.map[key].val
        return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.map:
            self.map[key].val = value
            self.cache.remove(self.map[key])
            self.cache.addFirst(self.map[key])
        else:
            if len(self.map) >= self.capacity:
                del self.map[self.cache.tail.prev.key]
                lastNode = self.cache.removeLast()
            newNode = Node(key, value)
            self.map[key] = newNode
            self.cache.addFirst(newNode)
