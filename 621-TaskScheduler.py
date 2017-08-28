import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        cnt = collections.Counter(tasks)
        # print cnt
        tmax = max(cnt.values())
        cnt2 = collections.Counter(cnt.values())
        # print cnt2
        mostFreqCount = cnt2[tmax]
        available_slots = (tmax - 1) * (n - mostFreqCount + 1)
        actual_slots = max(0, available_slots - (len(tasks) - mostFreqCount * tmax))

        return len(tasks) + actual_slots
