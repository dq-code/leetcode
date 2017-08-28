class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        dp = {}

        def helper(total, state):
            for i in range(maxChoosableInteger, 0, -1):
                if not state & (1 << (i - 1)):
                    if total + i >= desiredTotal:
                        dp[state] = True
                        return True
                    break

            for i in range(1, maxChoosableInteger + 1):
                if not state & (1 << (i - 1)):
                    temp_state = state | (1 << (i - 1))
                    if temp_state not in dp:
                        dp[temp_state] = helper(total + i, temp_state)

                    if not dp[temp_state]:
                        dp[state] = True
                        return True
            dp[state] = False
            return False

        if maxChoosableInteger >= desiredTotal: return True
        if (1 + maxChoosableInteger) * maxChoosableInteger < 2 * desiredTotal: return False
        return helper(0, 0)
