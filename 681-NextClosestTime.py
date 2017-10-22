class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        nums = [time[i] for i in range(len(time)) if time[i] in '0123456789']
        target = ''.join(time.split(':'))
        combs = []

        def valid(inputs):
            return 0 <= int(inputs[0:2]) <= 24 and 0 <= int(inputs[2:]) < 60

        def helper(comb):
            if len(comb) == len(nums):
                if comb not in combs:
                    combs.append(comb)
                return
            for i in range(len(nums)):
                helper(comb + nums[i])

        helper('')
        combs = sorted(combs)
        target_index = combs.index(target)
        combs = combs[target_index:] + combs[:target_index]
        # print combs
        right = 1
        index = 0
        while right < len(combs):
            if valid(combs[right]):
                index = right
                break
            right += 1

        return combs[index][0:2] + ":" + combs[index][2:]






