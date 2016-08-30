class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        if s == "": return 0
        if s[0] == "0": return 0
        dp = [0 for i in range(len(s) + 1)]
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s) + 1):
            subInt = int(s[i - 2:i])
            if subInt >= 10 and subInt <= 26:
                if subInt == 10 or subInt == 20:
                    dp[i] = dp[i - 2]
                else:
                    dp[i] = dp[i - 2] + dp[i - 1]
            elif s[i - 1] == '0':
                return 0
            else:
                dp[i] = dp[i - 1]

        return dp[-1]
