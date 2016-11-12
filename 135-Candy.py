class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candy = [1 for x in range(ratings)]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candy[i] = candy[i-1] + 1

        for i in range(len(ratings)-2, 0, -1):
            if ratings[i] > ratings[i+1] and candy[i] < candy[i+1]:
                candy[i] = candy[i+1] + 1

        return sum(candy)
