class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost): return -1

        remaining = 0
        startIndex = 0
        for i in range(len(gas)):
            if gas[i] + remaining < cost[i]:
                startIndex = i + 1
                remaining = 0
            else:
                remaining = gas[i] + remaining - cost[i]

        return startIndex
           