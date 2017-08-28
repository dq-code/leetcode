import collections
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        deque = collections.deque(s)

        for char in t:
            if not deque: return True
            if char == deque[0]:
                deque.popleft()

        return not deque
