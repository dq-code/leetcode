class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        isPrime = [True]*max(n,2)
        isPrime[0] = False
        isPrime[1] = False

        x = 2
        while x*x < n:
            if isPrime[x]:
                y = x*x
                while y < n:
                    isPrime[y] = False
                    y += x
            x += 1
        return sum(isPrime)