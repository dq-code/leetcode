class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = [1 for i in range(len(nums))]
        for i in range(len(nums)):
            walker = i
            # print "index %d"%i
            while nums[walker] != walker and nums[walker] != '-1' and nums[nums[walker]] != '-1':
                # print "inloop %d" % walker
                counter[nums[walker]] = counter[walker] + 1
                temp = walker
                walker = nums[temp]
                nums[temp] = '-1'
                # print counter
                # print nums
                # print walker
            nums[walker] = '-1'

        return max(counter)