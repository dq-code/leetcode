import collections

class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        counter = collections.Counter(secret)
        bulls = 0
        cows = 0
        for i in range(len(guess)-1, -1, -1):
            if guess[i] == secret[i]:
                bulls += 1
                counter[guess[i]] -= 1
        for i in range(len(guess) - 1, -1, -1):
            if guess[i] == secret[i]:
                continue
            if guess[i] in counter and counter[guess[i]]>0:
                counter[guess[i]] -= 1
                cows += 1

        return "%dA%dB"%(bulls,cows)
